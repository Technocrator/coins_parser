# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:08:33 2024

@author: 0
"""

# import the necessary packages
import numpy as np
import cv2
import matplotlib.pyplot as plt


# draw a rectangle
rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
plt.imshow(rectangle)
plt.show()
# draw a circle
circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
plt.imshow(circle)
plt.show()

bitwiseAnd = cv2.bitwise_and(rectangle, circle)
plt.imshow(bitwiseAnd)
plt.show()

bitwiseOr = cv2.bitwise_or(rectangle, circle)
plt.imshow(bitwiseOr)
plt.show()

bitwiseXor = cv2.bitwise_xor(rectangle, circle)
plt.imshow(bitwiseXor)
plt.show()

bitwiseNot = cv2.bitwise_not(circle)
plt.imshow(bitwiseNot)
plt.show()