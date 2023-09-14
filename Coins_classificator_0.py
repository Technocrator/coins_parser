import matplotlib
#Настроим matplotlib на выгрузку граффиков на диск, используя бэкнд agg
matplotlib.use("Agg")
#Подключаем необходимые пакеты
#Подключим бинаризатор меток, помогает перевести текствовые метки в двоичные
from sklearn.preprocessing import LabelBinarizer
#Подключим модуль, который поможет разделить выборки н аобучающую и тестовую
from sklearn.model_selection import train_test_split
#Подключим модуль, который поможет построить очтёт о работе модели
from sklearn.metrics import classification_report
#импортируем модель Sequential
from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import SGD
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import argparse
import random
import pickle
import cv2
import os

#создаём парсер аргуементов и передаём их

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help="Path to input dataset of images")
ap.add_argument("-m", "--model", required=True, help="path to output trained model")
ap.add_argument("-l","--label-bin", required=True, help="path to output label binarizer")
ap.add_argument("-p", "--plot", required=True, help="path to output accuracy/loss plot")

args = vars(ap.parse_args())
#dataset - путь к наботу изобраджений на диске
#model - наша модель будет сериализована и записана на диск. Этот аргумент содержит путь к выходному файлу модели.
#label-bin - метки набора данных сериализуются на диск для возможности их вызова в других скриптах. Это путь к выходному бинаризированному файлу меток.
#plot - путь к выходному файлу графика обучения.

#Теперь загрузим изображения и метки классов

print("[INFO] loading images...")
data = []
labels = []

#Берём пути к изображениям и рандомно перемешиваем

imagePaths = sorted(list(paths.list_images(args["dataset"])))
random.seed(42)
random.shuffle(imagePaths)

#Цикл по изображениям

for imagePath in imagePaths:
    #Загружаем изображением, меняем размер на 32х32 пикселей (без учета соотношения сторон)
    #сглаживаем его в 32х32х3 = 3072 пикселей и добавляем в список
    image = cv2.imread(imagePath)
    image = cv2.resize(image, (32,32)).flatten()
    data.append(image)

    #Извлекаем метку класса из пути к изображению и обновляем список меток

    label = imagePath.split(os.path.sep)[-2]
    labels.append(label)

