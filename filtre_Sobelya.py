import cv2
import numpy as np

#Путь к картинке
im_path = f'D:\python\coins_parser\pictures_dataset\cler_test_set\httpsstatic.auction.ruoffer_images2015122210bigIi5tV24qoZOe50_kopeek_1922_goda_sssr_pl.jpg'

#Считываем фото по указанному пути в двоичный объект
my_photo = cv2.imread(f"{im_path}")

# img_grey = cv2.cvtColor(my_photo, cv2.COLOR_BGR2GRAY)

#Зададим параметры матрицы для Фильтра Собеля

kernel = np.array([[-1,0,-1],[-2,0,2],[-1,0,1]])

kernel2 = np.array([[0,-1,0],[1,-2,1],[0,1,0]])

im = cv2.filter2D(my_photo, -1, kernel2)

cv2.imshow("Filtre Sobelya", im)

cv2.waitKey(0)
cv2.destroyAllWindows()