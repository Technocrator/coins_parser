import cv2 
import numpy as np 

image = cv2.imread("D:\\python\\coins_parser\\pictures_dataset\\10_kop_silver_sorted\\test\\coins\\coins1.jpg") 
#Фильтрация изображения
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
blur = cv2.GaussianBlur(gray, (5, 5), 0) 
thresh = cv2.threshold(blur, 0, 255,
cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)[1] 
# circles = cv2.HoughCircles(thresh,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)[0]
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 8,
                               param1=100, param2=30,
                               minRadius=1, maxRadius=30)
if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv2.circle(src, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv2.circle(src, center, radius, (255, 0, 255), 3)