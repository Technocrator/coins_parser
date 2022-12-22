# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 17:16:50 2022

@author: 0
"""

from selenium import webdriver
import time
import random
import selenium
from selenium.webdriver.common.keys import Keys

from fake_useragent import UserAgent



#Опции, которые мы будем передавать в браузер

options = webdriver.ChromeOptions() #Создадим экземпляр класса ChromeOpt

useragent = UserAgent()

#Отключаем ChromeDriver

options.add_argument('--disable-belink-features=AutonationControlled')

#Эта опция эмитирует юзер агента IE
options.add_argument(f"user-agent={useragent.ie}")

options.add_argument("--proxy-server=5.189.157.63:8080")
#Эта переменная хранит урл подключаемого сайта
url = 'https://auction.ru/auth'

#А этот url покажет твой user-agent

url_ua='https://www.whatismybrowser.com/detect/what-is-my-user-agent'

# driver = webdriver.Chrome(executable_path="d:\\python\\chromedriver")

#В переменной драйвер создаём объект класса webdriver.Crome
driver = webdriver.Chrome(executable_path="D:\\python\\chromedriver\\chromedriver.exe", options = options)

#Пробуем открыть страницу, адрес которой указан в переменной url
try:
    #Пробуем открыть страницу авторизации аукциона
    driver.get(url=url)
    
except Exception as ex:
    print(ex)

# finally:
#     driver.close()
#     driver.quit()