#В этом файле мы загружаем уже обученную ранее модель
#Подаём на вход изображение и получаем ответ, к какому классу оно относиться
#Импортируем необходимы пакеты

#load_model позволяет загрузить модель Keras с диска
from keras.models import load_model
import argparse
import pickle
import cv2

#Создаём парсер аргументов и передаём их
# --image  путь к входному изображению
# --model путь к нашей обученной и сериализованной модели
# --label-bin путь к бинаризатору меток
# --width ширина изображения для CNN. Должна соответсвовать конкретной модели
# --height высота входного изображения. Так же должна соответствовать конкретной модели
# --flatten надо  ли склаживать изображение (по умолчанию мы не будем этого делать)
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "path to input image we are going to classify")
ap.add_argument("-m","--model", required=True, help = "path to trained Keras model")
ap.add_argument("-l", "--label-bin", required=True, help="path to label binarizer")
ap.add_argument("-w", "--width", type = int, default=28, help="target spatial dimension width")
ap.add_argument("-e", "--height", type=int, default = 28, help="target spatial dimension height")
ap.add_argument("-f", "--flatten", type = int, default=-1, help="whether or not we should flatten the image")

args = vars(ap.parse_args())

#Загружаем входное изображение и меняем его размер на необходимый

image = cv2.imread(args["image"])
output = image.copy()
image = cv2.resize(image, (args["width"], args["height"]))

#Масштабируем значения пикселей к диапазону [0,1]

image = image.astype("float") / 255.0

#Если необходимо изображение можно сгладить
#Проверяем, необходимо ли сгладить изображение

if args["flatten"] < 0:
    image = image.flatten()
    image = image.reshape((1, image.shape[0]))
#В противном случае мы работаем с CNN - не сглаживаем изображение и просто добавляем размер пакета

else:
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))

#Теперь загрузим нашу модель и бинаризатор меток в память и попробуем распознать изображение
#Загружаем модель и бинаризатор меток

print("[INFO] loading network and label binarizer...")

model = load_model(args["model"])
lb = pickle.loads(open(args["label_bin"], "rb").read())

#Пытаемся классифицировать изображение

preds = model.predict(image)

#Находим индекс метки класса с наибольшей вероятностью соответствия

i = preds.argmax(axis=1)[0]
label = lb.classes_[i]

#Рисуем  метку класса + вероятность на выходном изображении

text = "{}: {:.2f}%".format(label, preds[0][i]*100)
cv2.putText(output, text,(10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

#Показываем выходное изображение

cv2.imshow("Image", output)
cv2.waitKey()