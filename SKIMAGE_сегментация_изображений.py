from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import skimage.segmentation as seg
import skimage.filters as filters
import skimage.draw as draw
import skimage.color as color
from skimage import data

#Простая функция для построения изображений

def image_show(image, nrows=1, ncols=1, cmap='gray'):
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(14,14))
    ax.imshow(image, cmap='gray')
    ax.axis('off')
    return fig,ax

image = data.page()


# image_show(image)

# fig, ax = plt.subplots(1,1)
# ax.hist(image.ravel(), bins=32, range=[0,256])

# ax.set_xlim(0, 256)

#Неконтролируемый порог

# text_threshold = filters.threshold_otsu
# image_show(image > text_threshold)

#Сегментация с алгоритмом для модели с учителем

image = io.imread(f'D:\python\coins_parser\pictures_dataset\cler_test_set\httpsstatic.auction.ruoffer_images2017012904bigOoAlIaiyJBV150_kopeek_1922_god_pl.jpg')

image_gray = color.rgb2gray(image)
image_show(image_gray)

#Активная контурная сегментация

def circle_points(resolution, center)


snake = seg.active_contour(image_gray, alpha=0.06, beta = 0.3)

fig, ax = image_show(image)

ax.plot()