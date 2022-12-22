# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 14:27:15 2022

@author: 0
"""

from selenium import webdriver
import time
import random
import selenium
from selenium.webdriver.common.keys import Keys
import pickle


from fake_useragent import UserAgent

options = webdriver.ChromeOptions() #Создадим экземпляр класса ChromeOpt

useragent = UserAgent()

options.add_argument(f"user-agent={useragent.ie}")

options.add_argument("--proxy-server=5.189.157.63:8080")
#Эта переменная хранит урл подключаемого сайта
url = 'https://auction.ru/auth'

#А этот url покажет твой user-agent

url_ua='https://www.whatismybrowser.com/detect/what-is-my-user-agent'

# driver = webdriver.Chrome(executable_path="d:\\python\\chromedriver")

#В переменной драйвер создаём объект класса webdriver.Crome
driver = webdriver.Chrome(executable_path="D:\\python\\chromedriver\\chromedriver.exe", options = options)

for cookie in pickle.load(open('cookies', 'rb')):
    driver.add_cookie(cookie)
    
time.sleep(2)

driver.refresh()