from selenium import webdriver
import time
import random

from fake_useragent import UserAgent


#Этот список будет хранить разные user_agent-ты для тестирования
user_agents_list = [
    "Hello World",
    "best_of_the_best",
    "python_today"
    ]

#Опции, которые мы будем передавать в браузер

options = webdriver.ChromeOptions() #Создадим экземпляр класса ChromeOpt

#Эта функция задаст парамерт user-agent браузера
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")

# options.add_argument(f"user-agent={random.choice(user_agents_list)}")


#Создадим объект класса UserAgent

useragent = UserAgent()

#Эта опция эмитирует юзер агента IE
# options.add_argument(f"user-agent={useragent.ie}")

# А эта опция эмитирует рандомного узерагента

options.add_argument(f"user-agent={useragent.random}")

options.add_argument("--proxy-server=138.128.91.65:8000")


#Эта переменная хранит урл подключаемого сайта
url = 'https://auction.ru/'

#А этот url покажет твой user-agent

url_ua='https://www.whatismybrowser.com/detect/what-is-my-user-agent'

# driver = webdriver.Chrome(executable_path="d:\\python\\chromedriver")

#В переменной драйвер создаём объект класса webdriver.Crome
driver = webdriver.Chrome(executable_path="chromedriver", options = options)

#Пробуем открыть страницу, адрес которой указан в переменной url
try:
    driver.get(url=url_ua)
    time.sleep(5)
except Exception as ex:
    print(ex)

# finally:
#     driver.close()
#     driver.quit()