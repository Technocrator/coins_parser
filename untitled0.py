# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:58:54 2024

@author: 0
"""

%matplotlib inline
import matplotlib.pyplot as plt
import skimage
import cv2
import numpy as np

img = cv2.imread('sample1.png')
plt.imshow(img), plt.show()
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# range for bills.
low_bill = np.array([0, 50, 0])
high_bill = np.array([100, 255, 255])

# range for coins.
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