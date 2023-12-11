import cv2 
import numpy as np 

image = cv2.imread("D:\\python\\coins_parser\\pictures_dataset\\10_kop_silver_sorted\\test\\coins\\coins1.jpg") 
#сначала переведём изображение в оттенки серого
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#заблурим изображение, т.е. сделаем размытым
blur = cv2.GaussianBlur(gray, (5, 5), 0) 
cv2.imshow('gray', blur)
#cv2.threshold делает изображение чернобелым возвращая список данных из которого нам нужен элемент с индексом 1. 
thresh = cv2.threshold(blur, 0, 255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)[1]


circles = cv2.HoughCircles(thresh,cv2.HOUGH_GRADIENT,1,20, param1=50,param2=30,minRadius=0,maxRadius=0)

print (circles)

# for i in circles:
#     cv2.circle(image,(i[0],i[1]),i[2],(0,0,255),2)
# cv2.imshow('Image', image)
# cv2.waitKey(0)