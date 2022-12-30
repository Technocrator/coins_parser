# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 13:23:24 2022

@author: 0
"""

import cv2
import numpy as np

#Путь к картинке
im_path = f'D:\python\coins_parser\pictures_dataset\cler_test_set\httpsstatic.auction.ruoffer_images2015122210bigIi5tV24qoZOe50_kopeek_1922_goda_sssr_pl.jpg'

#Считываем фото по указанному пути в двоичный объект
my_photo = cv2.imread(f"{im_path}")

#Применим к загруженной картинке метод медианного размытия с параметром 5

median_image = cv2.medianBlur(my_photo, 5)

#сделаем размытое изображение в оттенках серого

img_grey = cv2.cvtColor(median_image, cv2.COLOR_BGR2GRAY)

#Вызываем метод отображения картинки в отдельном окне. "image" - имя окна, my_photo - сама картинка
# cv2.imshow("image", my_photo)
# cv2.imshow("medianblur", median_image)
cv2.imshow("grey", img_grey)

#Установим параметр thresh, он же "зернистость"

thresh = 110

#Выделим контуры в изображении используя метод медианной фильтарции с параметром thresh 110

ret, thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)
cv2.imshow("thresh_img", thresh_img)

#Теперь обработаем полученное изображение и найдём контуры

contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Создадим пустое изображение для контуров

img_contours = np.zeros(my_photo.shape)

#Нарисуем контуры на пустом изображении

cv2.drawContours(img_contours, contours, -1, (255,255,255), 1)

#Отобразим получившийся результат на экране в отдельном окне

cv2.imshow('contours', img_contours)


#Эти две строчки обязательные, первая ждёт нажатия любой клавиши, а затем вторая дождавшись нажатия клавиши убивает окно
cv2.waitKey(0)
cv2.destroyAllWindows()