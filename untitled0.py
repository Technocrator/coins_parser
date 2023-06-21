# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 14:05:24 2023

@author: 0
"""

from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Conv2D, MaxPooling2D
from tensorflow.python.keras.layers import Activation, Dropout, Flatten, Dense

# Каталог с данными для обучения
train_dir = 'D:\\python\\coins_parser\\pictures_dataset\\10_kop_silver_sorted\\train'
# Каталог с данными для проверки
val_dir = 'D:\\python\\coins_parser\\pictures_dataset\\10_kop_silver_sorted\\val'
# Каталог с данными для тестирования
test_dir = 'D:\\python\\coins_parser\\pictures_dataset\\10_kop_silver_sorted\\test'
# Размеры изображения
img_width, img_height = 150, 150
# Размерность тензора на основе изображения для входных данных в нейронную сеть
# backend Tensorflow, channels_last
input_shape = (img_width, img_height, 3)
# Количество эпох
epochs = 30
# Размер мини-выборки
batch_size = 16
# Количество изображений для обучения
nb_train_samples = 3659
# Количество изображений для проверки
nb_validation_samples = 784
# Количество изображений для тестирования
nb_test_samples = 784