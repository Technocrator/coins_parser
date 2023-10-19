# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 11:31:03 2023

@author: 0
"""

#Скрипт для обучения сети Small
# импортируем бэкенд Agg из matplotlib для сохранения графиков на диск
import matplotlib
matplotlib.use("Agg")
 
# подключаем необходимые пакеты
from smallvggnet import SmallVGGNet
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import SGD
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import argparse
import random
import pickle
import cv2 
import os

#Данные будут дополняться с помощь ImageDataGenerator

#создаём парсер аргументов и передаём их

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
    help="path to input dataset of images")
ap.add_argument("-m", "--model", required=True,
    help="path to output trained model")
ap.add_argument("-l", "--label-bin", required=True,
    help="path to output label binarizer")
ap.add_argument("-p", "--plot", required=True,
    help="path to output accuracy/loss plot")
args = vars(ap.parse_args())

#Загружаем и предварительно обрабатываем данные
#Инициализируем данные и метки

print ("[INFO] loading images..." )
data = []
labels = []

#Берём пути к изображениям и рандомно перемешиваем
imagePaths = sorted(list(paths.list_images(args["dataset"])))
random.seed(42)
random.shuffle(imagePaths)

#Цикл по изображениям
for imagePath in imagePaths:
    #Загружаем изображение, меняем размер на 64х64 пиклесей
    #(требуемые размеры для SmallVGGNet), изменённое изображение добавляем в список
    image = cv2.imread(imagePath)
    image = cv2.resize(image, (64, 64))
    data.append(image)
    
    #Извлекаем метку класса из пути к изображению и обновляем список меток
    
    label = imagePath.split(os.path.sep)[-2]
    labels.append(label)
    
#Масштабируем интенсивности пикселей в диапазон [0, 1]

data = np.array(data, dtype="float") / 255.0
labels = np.array(labels)

#Разделяем данные на обучающую и тестовую выборки и бинаризируем метки
#Разбиваем данные на обучающую и тестовую выборки, используя 75% данных
#Для обучения и оствшиеся 25% для тестирования
(trainX, testX, trainY, testY) = train_test_split(data, labels, test_size=0.25, random_state = 42)
#Конвертируем метки из целых чисел в векторы (для 2х классов при бинарной классификации вам следует
# использовать функцию Keras to_categorical вместо LabelBinarizer из scikit_learn,
# которая не возвращает вектор

lb = LabelBinarizer()
trainY = lb.fit_transform(trainY)
testY = lb.transform(testY)

#Теперь дополняем данные
#Создаём генератор для добавления изображений
#Этот генератор позволит нам создать дополнительные данные из уже существующих путём поворота, сдвига, обрезания и увеличения изображений.
aug = ImageDataGenerator(rotation_range=30, width_shift_range=0.1, height_shift_range=0.1, shear_range=0.2, horizontal_flip=True, fill_mode="nearest")

#Инициируем нашу VGG-подобную свёрточную нейросеть
#Чтобы собрать нашу SmallVGGNet, просто вызовем метод SmallVGGNet.build
model = SmallVGGNet.build(width=64, height=64, depth=3, classes=len(lb.classes_))

#Скомпилируем и обучим модель.
#Инициализируем скорость обучения, общее число шагов и размер пакета

INIT_LR = 0.1
EPOCHS = 7
BS = 32

# компилируем модель с помощью SGD (для бинарной классификации следует испольдовать
# binary_crossentropy)

print ("[INFO] traning network...")

opt = SGD(lr=INIT_LR, decay=INIT_LR / EPOCHS)
model.compile(loss="categorical_crossentropy", optimizer=opt,
    metrics=["accuracy"])
 
# обучаем нейросеть
H = model.fit_generator(aug.flow(trainX, trainY, batch_size=BS),
    validation_data=(testX, testY), steps_per_epoch=len(trainX) // BS,
    epochs=EPOCHS) 

# сохраняем модель и бинаризатор меток на диск
print("[INFO] serializing network and label binarizer...")
model.save(args["model"])
f = open(args["label_bin"], "wb")
f.write(pickle.dumps(lb))
f.close()

# оцениваем нейросеть
print("[INFO] evaluating network...")
predictions = model.predict(testX, batch_size=32)
print(classification_report(testY.argmax(axis=1),
     predictions.argmax(axis=1), target_names=lb.classes_))
 
#строим графики потерь и точности
N = np.arange(0, EPOCHS)
plt.style.use("ggplot")
plt.figure()
plt.plot(N, H.history["loss"], label="train_loss")
plt.plot(N, H.history["val_loss"], label="val_loss")
plt.plot(N, H.history["accuracy"], label="train_acc")
plt.plot(N, H.history["val_acc"], label="val_acc")
plt.title("Training Loss and Accuracy (SmallVGGNet)")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend()
plt.savefig(args["plot"])

