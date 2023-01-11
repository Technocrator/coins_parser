import cv2
import numpy as np


my_photo = cv2.imread(f'D:\python\coins_parser\pictures_dataset\cler_test_set\httpsstatic.auction.ruoffer_images2016050408big99WLtxIKPZURdve_monety_odnim_lotom_50_kopeek_1922_goda_i_50_kopeek_1987_goda_otlichnoe_sostojanie.jpg')
#my_photo = cv2.imread('bricks\\White1.jpg')
img_grey = cv2.cvtColor(my_photo,cv2.COLOR_BGR2GRAY)

img_grey = cv2.medianBlur(img_grey, 5)

my_photo = cv2.medianBlur(my_photo, 5)

rows = img_grey.shape[0]
circles = cv2.HoughCircles(img_grey, cv2.HOUGH_GRADIENT, 1, rows / 8,
                          param1=100, param2=100,
                          minRadius=1, maxRadius=500)

res = np.zeros(my_photo.shape)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center = (i[0], i[1])
        # circle center
        cv2.circle(my_photo, center, 1, (0, 100, 100), 3)
        # circle outline
        radius = i[2]
        cv2.circle(my_photo, center, radius, (255, 0, 255), 3)

cv2.imshow('origin', my_photo) # выводим итоговое изображение в окно

cv2.waitKey()
cv2.destroyAllWindows()