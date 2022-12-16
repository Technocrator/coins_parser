from selenium import webdriver
import time
import random
import selenium

from fake_useragent import UserAgent



#Опции, которые мы будем передавать в браузер

options = webdriver.ChromeOptions() #Создадим экземпляр класса ChromeOpt

useragent = UserAgent()


#Эта опция эмитирует юзер агента IE
options.add_argument(f"user-agent={useragent.ie}")

#Эта переменная хранит урл подключаемого сайта
url = 'https://auction.ru/auth'

#А этот url покажет твой user-agent

url_ua='https://www.whatismybrowser.com/detect/what-is-my-user-agent'

# driver = webdriver.Chrome(executable_path="d:\\python\\chromedriver")

#В переменной драйвер создаём объект класса webdriver.Crome
driver = webdriver.Chrome(executable_path="chromedriver", options = options)

#Пробуем открыть страницу, адрес которой указан в переменной url
try:
    driver.get(url=url)
    time.sleep(5)
    
    email_input = driver.find_element("class_name", 'form__control form__control_block')
    print(email_input)
    
except Exception as ex:
    print(ex)

# finally:
#     driver.close()
#     driver.quit()