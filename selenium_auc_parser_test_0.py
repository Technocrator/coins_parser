
import selenium
from selenium import webdriver
from fake_useragent import UserAgent
import requests
import datetime

#Эта функция примет начальный индекс имени файла и байтовый массив, который затем сохранит в файл картинки формата .jpg
def save_func(src, image_bytes):
    #Откроем файл для записи двоичной информации с атрибутом wb и запишем в него переданные байты
    fn=src.replace(":","").replace("/","")
    with open (fn, "wb") as file:
        file.write(image_bytes)

options = webdriver.ChromeOptions()
useragent = UserAgent()

#Представимся useragent-ом как браузер IE
options.add_argument(f"user-agent = {useragent.ie}")

#Адрес лота, где содержаться картинки
url = "https://auction.ru/offer/rubl_1898_parizh_nechastyj_khoroshee_sostojanie_xf_fotr1069-i241971265377629.html"

driver = webdriver.Chrome(executable_path="D:\\python\\chromedriver\\chromedriver.exe",options = options)
driver.get(url=url)

#Находим ссылки на картинки с лотом
img = driver.find_elements_by_class_name("fotorama__img")

#В этом цикле загружаем содержимое каждой картинки в виде байтов и вызываем функцию save_func для сохранения их в файлы картинок на диске
for e,i in enumerate(img):
    src = i.get_attribute('src')
    print(src)
    image_bytes = bytes(requests.get(src).content)
    save_func(str(src), image_bytes)
    

