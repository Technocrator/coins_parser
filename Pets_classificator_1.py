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

# Теперь мы легко можем применить операции с массивами к нашим данным и меткам
# Масштабируем интенсивности пикселей в диапазон [0,1]

data = np.array(data, dtype="float") / 255.0
labels = np.array(labels)

#Разбиваем данные на обучающую и тестовую выборки, используя 75% данных для обучения и оставшиеся 25% для тестирования
#train_test_split разделит для нас данные. trainX и testX - это изображения, trainY и testY соответствующие метки.
(trainX, testX, trainY, testY) = train_test_split(data, labels, test_size = 0.25, random_state=42)

#Конвертируем метки из целых чисел в векторы (для 2х классов при бинарной классификации вам следует
# использовать функцию Keras "to_categorical" вместо "LabelBinarizer" из scikit-learn,
# которая не возвращает вектор)

lb = LabelBinarizer()
#fit_transform находит все уникальные метки класса в testY, а затем преобразует их в метки One-Hot Encoding
#Вызов .transform выполняет всего один шаг One-Hot Encoding - уникальный набор возможных меток классов уже был определен вызовом fit_transform
trainY = lb.fit_transform(trainY)
testY = lb.fit_transform(testY)

#Следующий шаг - определение архитектуры нашей нейронной сети с использованием Keras. Мы будем использовать сеть с одним входным слоем
#одним выходным и двумя скрытыми.
#Определим архитектуру 3072-1024-512-3 с помощью Keras

model = Sequential()
model.add(Dense(1024, input_shape=(3072,), activation="sigmoid"))
model.add(Dense(512,activation="sigmoid"))
model.add(Dense(len(lb.classes_), activation="softmax"))

#После того, как мы определили архитектуру нашей нйронной сети, нам необходимо скомпилировать её
#инициализируем скорость обучения и общее число эпох

INIT_LR = 0.01
EPOCHS = 75

#Компилируем модель, используя SGD как оптимизатор и категориальную кросс-энтропию
#в качестве функции потерь (для бинарной классификации следует использовать binary_crossentropy)

print ("[INFO] training network...")

opt = SGD(lr=INIT_LR)
model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=["accuracy"])

#Теперь, когда наша модель Keras скомпилирована, мы можем "подогнать" (fit) (т.е. обучить) её
#обучаем нейросеть

H = model.fit(trainX, trainY, validation_data=(testX, testY), epochs=EPOCHS, batch_size=32)

#Мы обучили модель, теперь нужно оценить её с помощью тестовой выборки
#Для оценки модели Keras можно использовать комбинацию методов .predict и classification_report из scikit-learn
#Оцениваем нейросеть

print("[INFO] evaluating network...")
predictions = model.predict(testX, batch_size=32)
print(classification_report(testY.argmax(axis=1), predictions.argmax(axis=1), target_names=lb.classes_))

#Сохраним нашу модель на диск

print ("[INFO] serializing network and label binarizer...")
model.save(args["model"])
f = open(args["label_bin"], "wb")
f.write(pickle.dumps(lb))
f.close()

#Строим граффик потерь и точности

# N = np.arange(0, EPOCHS)
# plt.style.use("ggplot")
# plt.figure()
# plt.plot(N, H.history["loss"], label="train_loss")
# plt.plot(N, H.history["val_loss"], label = "val_loss")
# plt.plot(N, H.history["acc"], label = "train_acc")
# plt.plot(N, H.history["val_acc"], label = "val_acc")
# plt.title("Traning Loss and Accuracy (Simple NN)")
# plt.xlabel("Epoch #")
# plt.ylabel("Loss/Accuracy")
# plt.legend()
# plt.savefig(args["plot"])

print (H.history)
