from skimage import data
from skimage import io
import numpy as np
import matplotlib.pyplot as plt

image = data.binary_blobs()

plt.imshow(image, cmap='gray')

#Импорт цветного изображения из библиотеки skimage

image = data.astronaut()
plt.imshow(image)

#Cчитываем картинку из файла и выводим на экран

image = io.imread(f'D:\python\coins_parser\pictures_dataset\cler_test_set\httpsstatic.auction.ruoffer_images2017012904bigOoAlIaiyJBV150_kopeek_1922_god_pl.jpg')
plt.imshow(image)

#Загрузка нескольких изображкний

images = io.ImageCollection(f'D:\python\coins_parser\pictures_dataset\cler_test_set\*.jpg')

print('Тип полученных данных :', type(images))
print(images.files)

#сохранение изображений

image = data.astronaut()
io.imsave('logo.png', image)