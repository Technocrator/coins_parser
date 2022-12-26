# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 14:30:49 2022

@author: 0
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 14:08:33 2022

@author: 0
"""

from selenium import webdriver
import time
import random
import selenium
from selenium.webdriver.common.keys import Keys
import pickle
import datetime


from fake_useragent import UserAgent


start_time = datetime.datetime.now()
#Опции, которые мы будем передавать в браузер

options = webdriver.ChromeOptions() #Создадим экземпляр класса ChromeOptions

#Создадим экземпляр класса UserAgent
useragent = UserAgent()


#Эта опция эмитирует юзер агента IE
options.add_argument(f"user-agent={useragent.ie}")


# options.add_argument("--proxy-server=5.189.157.63:8080")

#Эта опция заставит выполняться окно браузера в фоновом режиме
# options.headless = True


#Эта переменная хранит урл подключаемого сайта


url = 'https://m.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB~pm7gmmZw?radius=0&presentationType=serp'

#А этот url покажет твой user-agent

url_ua='https://www.whatismybrowser.com/detect/what-is-my-user-agent'

# driver = webdriver.Chrome(executable_path="d:\\python\\chromedriver")

#В переменной драйвер создаём объект класса webdriver.Crome
driver = webdriver.Chrome(executable_path="D:\\python\\chromedriver\\chromedriver.exe", options = options)

#Пробуем открыть страницу, адрес которой указан в переменной url
try:
    #Пробуем открыть страницу авторизации аукциона
    driver.get(url=url)
    time.sleep(5)
    
    
    #ВЫведем на пеечать номер текущей вкладки
    print(driver.window_handles)
    print(driver.current_url)
    
    #На странице авторизации находим поле ввода логина
    # email_input = driver.find_element_by_name("email_or_login")
    # #очищаем его
    # email_input.clear()
    # #Передаём логин
    # email_input.send_keys("kerinchen@rambler.ru")
    # # print(email_input[0])
    # #Находим поле ввода пароля
    # email_input = driver.find_element_by_name("password")
    # #передаём пароль
    # email_input.send_keys("Kro4t8jruhaakfjgkri35ytaj")
    # time.sleep(1)
    # # email_input.find_element_by_id('auth_btn').click()
    # #Передаём нажатие кавиши ENTER
    # email_input.send_keys(Keys.ENTER)
    
    #Найдём заголовок h3 с параметром itemprop='name'
    items = driver.find_elements_by_xpath("//h3[@itemprop='name']")
    # time.sleep(2)
    driver.implicity_wait(5)
    #Кликнем на ранее найденный заголовок
    items[0].click()
    
    #ВЫведем на пеечать номер текущей вкладки
    print(driver.window_handles)
    print(driver.current_url)
    
    #Далее по вкладкам можно перемещать используя индекс элемента driver.window_handles
    
    driver.switch_to.window(driver.window_handles[1])
    print(driver.current_url)
    
    #Найдём имя продавца по классу
    
    username = driver.find_element_by_class_name("text-text-LurtD text-size-ms-_Zk4a")
    
    print(username.text)
    
    # time.sleep(1)
    driver.implicity_wait(5)
    #Закроем окошко
    
    driver.close()
    
    #вернёмся на первую страниццу
    
    driver.switch_to.window(driver.window_handles[0])
    # time.sleep(0.5)
    driver.implicity_wait(5)
    #Откроем следующий лот
    
    items[1].click()
    
    
    
except Exception as ex:
    print(ex)

finish_time = datetime.datetime.now()

spent_time = finish_time - start_time

print(spent_time)

# finally:
#     driver.close()
#     driver.quit()