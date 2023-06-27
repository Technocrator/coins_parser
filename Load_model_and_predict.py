#подключим библиотеку импорта ранее обученной модели

from tensorflow.keras.models import load_model
#from tensorflow.keras.models import load_weights
import os
import numpy as np
import pandas as pd
# from tensorflow.keras.utils import load_img
# from tensorflow.keras.utils import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator

#с помощью метода load_model загрузим ранее обученную модель
model = load_model('D:\\python\\coins_parser\\coins_parser\\coins_model_1')
model.load_weights('D:\\python\\coins_parser\\coins_parser\\first_model_weights.h5')

#Укажим путь к директории с контрольным набором данных

control_dir = 'D:\\python\\coins_parser\\pictures_dataset\\10_kop_silver_sorted\\control\\'

#Создадим функцию считывающую изображение и конвертирующую его в бинарный массив

def load_image(img_path, show=True):
    #Эта команда считывает картинку в двоичном виде
    img_original = load_img(img_path)
    #Эта команда преобразует картинку к размеру 150на150 пикселей
    img = load_img(img_path, target_size=(150,150))
    #Эта команда преобразует картинку в массив
    img_tensor = img_to_array(img)
    #команда np.expand_dims добавит ещё одну ось(измерение) в начало массива
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255
    
    return img_tensor

#Создадим функцию предстказания, которая получает на вход путь к конкретной картинке
#Затем вызывает функцию load_image, которая преобразует картинку в массив
#и в конце полученный массив передаёт раннее обученной модели с целью классификации изображения

def predict(img_file):
    new_image = load_img(img_file)
    pred = model.predict(new_image)
    return pred

#Подготавливаем Data Set
#Загрузим список имён всех картинок в указанном ранее каталоге
# coins_set = os.listdir(control_dir)

# df_coins_set = pd.DataFrame(coins_set)
# df_coins_set['path'] = control_dir
# df_coins_set = df_coins_set.reset_index()
# df_coins_set = df_coins_set['path']+df_coins_set[0]

# results = []

# for i in range(len(df_coins_set)):
#     results.append(predict(df_coins_set[i]))
    

# print(results)

# for i in range(len(df_coins_set)):
#     print(predict(df_coins_set[i]))

img = 'D:\\python\\coins_parser\\pictures_dataset\\10_kop_silver_sorted\\control\\1.jpg'

print(predict(img))