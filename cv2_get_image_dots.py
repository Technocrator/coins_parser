import cv2
import numpy as np

#Путь к картинке
im_path = f'D:\python\coins_parser\pictures_dataset\cler_test_set\httpsstatic.auction.ruoffer_images2015122210bigIi5tV24qoZOe50_kopeek_1922_goda_sssr_pl.jpg'

#Считываем фото по указанному пути в двоичный объект
image = cv2.imread(f"{im_path}")

operatedImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

operatedImage = np.float32(operatedImage)

dest = cv2.cornerHarris(operatedImage, 2, 5, 0.07)

dest = cv2.dilate(dest, None)

image[dest > 0.01 * dest.max()] = [0,0,255]

cv2.imshow('Image with Borders', image)

cv2.waitKey(0)
cv2.destroyAllwindows()