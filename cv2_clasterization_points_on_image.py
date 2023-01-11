import cv2, math, time
import numpy as np

#Эта функция вычисляет расстояние между точками

def get_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    #Вычисляем Евклидово расстояние между точками
    l = math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
    return l
    

#Эта функция будет вычислять центр масс точек

def get_center(centers, point):
    l = len(centers)
    res =-1
    min_r = 9999999999999.0
    for i in range(0, l):
        center = centers[i]
        x,y,count = center
        r = get_distance(point,(x,y))
        if r >= 10:
            continue
        if r < min_r:
            res = i
            min_r = r
    return res
        

#Эта функция добавит точку в центр масс

def add_to_center(center, point):
    x1,y1,count = center
    count += 1
    x2,y2 = point
    x=x1+(x2-x1)/float(count)
    y=y1+(y2-y1)/float(count)
    return x,y,count

#Путь к картинке
im_path = f'D:\python\coins_parser\pictures_dataset\cler_test_set\httpsstatic.auction.ruoffer_images2015122210bigIi5tV24qoZOe50_kopeek_1922_goda_sssr_pl.jpg'

#Считываем фото по указанному пути в двоичный объект
image = cv2.imread(f"{im_path}")

#Конвертируем исходное изображение в цветовое пространство в оттенках серого

operatedImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Изменим тип данных на 32х битный с плавающей запятой

operatedImage = np.float32(operatedImage)

#Применим метод cv2.cornerHarris для определения углов с соответсвующими значениями в качестве входных параметров

dest = cv2.cornerHarris(operatedImage, 2,5, 0.07)

#Будем использовать метод dilate что бы отметить углы возвращённого изображения

dest = cv2.dilate(dest, None)

# Создадим исходное изображение с оптимальными пороговыми значениями

img_blank = np.zeros(image.shape)

#Вернём исходное изображение с оптимальным пороговым значением и указаним цвета угла.
img_blank[dest > 0.05 * dest.max()] = [0,0,255]

#Сначала создадим список точек

heigh = img_blank.shape[0]

width = img_blank.shape[1]

points=[]

for x in range(0, width):
    for y in range(0, heigh):
        
        if img_blank[y,x,2] == 255:
            points.append((x,y))

#Теперь обработаем полученный список
points_count = len(points)
print("количество обрабатываемых точкек: ", points_count)

beg_time = time.perf_counter()

centers = []

for i in range(0, points_count):
    point = points[i]
    center_index = get_center(centers, point)
    if center_index == -1:
        x, y = point
        centers.append((x,y,1))
    else:
        center = centers[center_index]
        centers[center_index] = add_to_center(center, point)

end_time = time.perf_counter()

print ("Прошло времени ", end_time - beg_time)

print ("Осталось точек ", len(centers))

img_blank1 = np.zeros(image.shape)

for center in centers:
    x, y, count = center
    img_blank1[int(y), int(x), 2] = 255
    
#Окно с выводимым изображением с углами

cv2.imshow('Image with Borders', img_blank1)

if cv2.waitKey(0) & 0xff ==27:
    cv2.destroyAllWindows()