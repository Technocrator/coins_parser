# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:58:54 2024

@author: 0
"""
#Подключаем нужные библиотеки
%matplotlib inline
import matplotlib.pyplot as plt
import skimage
import cv2
import numpy as np

#Импортируем картинку 
img = cv2.imread('D:\\python\\sample1.png')
#img = cv2.imread('D:\\python\\coins_parser\\pictures_dataset\\10_kop_silver_sorted\\coins\\httpsstatic.auction.ruoffer_images2015081312smallSSxcFRjyjezP10_desjat_kopeek_1910_spb_eb_kop_serebro.jpg')
#Прорисуем изначальное изображение
plt.imshow(img), plt.show()
#Применим фильтр cvtColor, превращающий цветное изображение в чб
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Установим границы порогового цветового значения для прямоугольника
low_bill = np.array([0, 50, 0])
high_bill = np.array([100, 255, 255])

# Установим границы порогового цветового значения для монеты
low_coin = np.array([120, 50, 0])
high_coin = np.array([240, 255, 255])

# make masks for each bill and coin.
mask_bill = cv2.inRange(hsv_img, low_bill, high_bill)
mask_coin = cv2.inRange(hsv_img, low_coin, high_coin)

# Extract bills and coins using logical operator.
bill = cv2.bitwise_and(hsv_img, hsv_img, mask=mask_bill)
coin = cv2.bitwise_and(hsv_img, hsv_img, mask=mask_coin)

# plot.
plt.subplot(1,2,1)
plt.title('Bills')
plt.imshow(bill)
plt.subplot(1,2,2)
plt.title('Coins')
plt.imshow(coin)
plt.show()

# find contours.
ret_bill,thresholded_bill = cv2.threshold(bill[:,:,2],0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
contours_bill, hier_bill = cv2.findContours(thresholded_bill, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
ret_coin,thresholded_coin = cv2.threshold(coin[:,:,2],0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
contours_coin, hier_coin = cv2.findContours(thresholded_coin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# draw contours.
cont_draw_bill = np.zeros(thresholded_bill.shape)
cv2.drawContours(cont_draw_bill, contours_bill, -1, (255, 0, 0), 3)
cont_draw_coin = np.zeros(thresholded_coin.shape)
cv2.drawContours(cont_draw_coin, contours_coin, -1, (255, 0, 0), 3)
plt.subplot(1,2,1)
plt.title('Bills')
plt.imshow(cont_draw_bill, cmap='gray')
plt.subplot(1,2,2)
plt.title('Coins')
plt.imshow(cont_draw_coin, cmap='gray')
plt.show()

num_contour = len(contours_bill)
indices = range(num_contour)
for contour, index in zip(contours_bill, indices):
    x, y, w, h = cv2.boundingRect(contour)
    plt.subplot(1, num_contour, index+1)
    plt.title(str(index+1) + 'th bill')
    plt.imshow(img[y:y+h, x:x+w])
plt.show()

# coins.
num_contour = len(contours_coin)
indices = range(num_contour)
for contour, index in zip(contours_coin, indices):
    x, y, w, h = cv2.boundingRect(contour)
    plt.subplot(1, num_contour, index+1)
    plt.title(str(index+1) + 'th bill')
    plt.imshow(img[y:y+h, x:x+w])
plt.show()

