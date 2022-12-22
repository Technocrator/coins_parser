from selenium import webdriver
import time
import random
import selenium
from selenium.webdriver.common.keys import Keys
import pickle


from fake_useragent import UserAgent



#Опции, которые мы будем передавать в браузер

options = webdriver.ChromeOptions() #Создадим экземпляр класса ChromeOpt

useragent = UserAgent()


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
    time.sleep(5)
    #На странице авторизации находим поле ввода логина
    email_input = driver.find_element_by_name("email_or_login")
    #очищаем его
    email_input.clear()
    #Передаём логин
    email_input.send_keys("kerinchen@rambler.ru")
    # print(email_input[0])
    #Находим поле ввода пароля
    email_input = driver.find_element_by_name("password")
    #передаём пароль
    email_input.send_keys("Kro4t8jruhaakfjgkri35ytaj")
    time.sleep(1)
    # email_input.find_element_by_id('auth_btn').click()
    #Передаём нажатие кавиши ENTER
    email_input.send_keys(Keys.ENTER)
    
    pickle.dump(driver.get_cookies(), open('cookies','wb'))
    
except Exception as ex:
    print(ex)

# finally:
#     driver.close()
#     driver.quit()