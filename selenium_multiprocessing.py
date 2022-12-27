
from selenium import webdriver
import time
import random
import selenium
from selenium.webdriver.common.keys import Keys
import pickle
import datetime
from multiprocessing import Pool


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


#Пробуем открыть страницу, адрес которой указан в переменной url
# try:
#     #Пробуем открыть страницу авторизации аукциона
#     driver.get(url=url)
#     time.sleep(5)

urls_list=["https://auction.ru/offer/rar_ot_rublja_redkij_khoroshij_1_rubl_1900_fz_smotrite_drugie_moi_loty_ne_v_tope-i243349032726997.html", "https://auction.ru/offer/rubl_1898_parizh_nechastyj_khoroshee_sostojanie_xf_fotr1069-i241971265377629.html", "https://auction.ru/offer/rubl_1899_fz_porezhe_ochen_khoroshee_sostojanie_xf_relef_br22035-i243785587238849.html", "https://auction.ru/offer/rubl_1896_ag_porezhe_khoroshee_sostojanie_xf_fotr868-i232199685991760.html"]

def get_data(url):
    
    try:
        
        driver = webdriver.Chrome(executable_path="D:\\python\\chromedriver\\chromedriver.exe", options = options)
        driver.get(url=url)
        time.sleep(5)
        #Эта команда сделает снимок и сохранит его в файл
        driver.get_screenshot_as_file("1.png")
    except Exception as ex:
        print(ex)
        
        
        
    finally:
        # driver.close()
        driver.quit()

# finally:
#     driver.close()
#     driver.quit()

if __name__ == "__main__":
    
    # for url in urls_list:
    #     get_data(url)

    #Создадим мультипроцессорный объект класса Pool
    p = Pool(processes = 1)
    
    #Вызываем метод map, который заставляет выполнят вызываемую функцию относительно каждого итерируемого объекта
    p.map(get_data, urls_list)