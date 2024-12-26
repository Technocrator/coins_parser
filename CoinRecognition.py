# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 16:22:55 2024

@author: 0
"""

#Этот скрипт распознаёт монеты и купюры на изображении, выделяя их цветом

#Импортируем нужные библиотеки
%matplotlib inline
import matplotlib.pyplot as plt
import skimage
import cv2
import numpy as np

#Считаем исходное изображение из файла и прорисуем его на экране
img = cv2.imread("D:\\python\\sample1.png")
plt.imshow(img)
plt.show()

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#определим диапазон цветовых значений для купюры
low_bill = np.array([0,50,0])
high_bill = np.array([100,255,255])

#определим диапазон цветовых значений для монеты
low_coin = np.array([120,50,0])
high_coin = np.array([240,255,255])

#Сделаем маски для каждой купюры и монеты

д

