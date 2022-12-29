import selenium
from selenium import webdriver
from fake_useragent import UserAgent
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import requests
from bs4 import BeautifulSoup as BS
from time import sleep
import os
from random import random, randrange




class Ui_MainWindow(object):
    #В этой функции создаются и прописываются параметры основных элементов окна
    def setupUi(self, MainWindow):
        #Создаём объект MainWindow
        MainWindow.setObjectName("MainWindow")
        #Задаём размеры 800*600
        MainWindow.resize(800, 600)
        #Создаём объект CentralWidget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        #Присваеваем ему имя
        self.centralwidget.setObjectName("centralwidget")
        #создадим большое тесстовое поле
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(90, 170, 451, 341))
        self.textEdit.setObjectName("textEdit")
        #создадим строку ввода запроса
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 80, 451, 20))
        self.lineEdit.setObjectName("lineEdit")
        #создадим метку с подписью
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 50, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        #создадим поисковую кнопку
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.search_func)
        #создадим кнопку запуска парса картинок
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 110, 95, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.parse_func)
        #создание вкладок меню
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Поисковый запрос"))
        self.pushButton.setText(_translate("MainWindow", "ПОИСК"))
        
        self.pushButton_2.setText(_translate("MainWindow", "СКАЧАТЬ ФОТО"))
        self.menu.setTitle(_translate("MainWindow", "Поиск"))
    
    #Эта функция обраатывает нажатие кнопки Поиск
    def search_func(self):
        self.user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
        #зададим переменную, которая будет хранить первую чатсть адреса, к тоторому мы будем присоеденять поисковый запрос
        search_const = 'https://auction.ru/listing/offer/search_'
        #В эту переменную к поисковой константе доабаляется содержимое текстового поля, введённого пользователем
        search_string = search_const + self.lineEdit.text()
        #результат выводим в большое текстовое поле
        self.textEdit.append("Осуществляю поиск по запросу: " + self.lineEdit.text())
        #sleep(3)
        #Запрашиваем поисковую строку с результатами поиска по поисковому запросу
        r = requests.get(search_string, headers = self.user_agent)
        #Создаём объект BeautifulSoup
        html = BS(r.text, 'html.parser')
        #self.textEdit.append(html.text)
        #Находим тег "а" пагинатора, который содержит обдее количество страниц пагинации с этим запросом
        paginator_count = html.find('a', class_ = 'listing__pager__link').text
        #Покажем в текстовом поле предварительную информацию о найденых лотах
        self.textEdit.append("По запросу: " + self.lineEdit.text() + " найдено страниц: " + paginator_count)
        self.lots_a_tags = html.findAll('a', class_= 'offers__item__title')
        self.lots_links = []
        for a in self.lots_a_tags:
            self.lots_links.append('https://auction.ru'+a['href'])
        
        #В этом цикле генерируются ссылки на все страницы пагинации путём добавления к первой странице с результатами поиска '?pg=' + номер страницы по возврастающей
        #так же каждая страница парситься и из неё вытягиваются ссылки на лоты
        for i in range (1, int(paginator_count)):
            #Между запросами страницы поставим паузу 1 сек... да долго
            sleep(1)
            #сформируем очередную ссылку для парсенья
            paginator_link = search_string+'?pg='+str(i)
            #Выполним запрос к страницы
            r = requests.get(paginator_link, headers = self.user_agent)
            html = BS(r.text, 'html.parser')
            #найдём все интересующие нас тэги а
            self.lots_a_tags = html.findAll('a', class_= 'offers__item__title')
            #вытащим из всех тэгов "а" ссылки и добавим к началу каждой из них 'https://auction.ru' 
            for a in self.lots_a_tags:
                self.lots_links.append('https://auction.ru'+a['href'])
        #запишем получившийся массив ссылок в файл, имя файла возьмём из строки поискового запроса
        fname = self.lineEdit.text()+'.txt'
        srch_str=self.lineEdit.text()
        try:
            os.mkdir(f"D:\python\coins_parser\pictures_dataset\{srch_str}")
        #Если такая директория уже существует, выведем об этом сообщение в текстовое поле
        except FileExistsError:
            self.textEdit.append('Каталог ' + fname+'_set' + ' уже существует')
        f = open(f"D:\python\coins_parser\pictures_dataset\{srch_str}\\{fname}", 'a')
        for lot in self.lots_links:
            
            f.write(str(lot+'\n'))
        f.close()
        
        self.textEdit.append('Найдено: ' + str(len(self.lots_links)) + ' лотов')
        self.textEdit.append('Ссылки записаны в файл: ' + fname)
    
        
    
    #Эта функция примет начальный индекс имени файла и байтовый массив, который затем сохранит в файл картинки формата .jpg
    def save_func(self, dir_name,src, image_bytes):
        #Очистим имя файла от ненужных символов
        fn=src.replace(":","").replace("/","")
        #Откроем файл для записи двоичной информации с атрибутом wb и запишем в него переданные байты
        #полный путь к файлу формируется из переменной dir_name и очищенного имени файла
        #переменная image_bytes содержит двоичный код картинки, в дальнейшем сохраняемой на диск
        with open (f"{dir_name}\{fn}", "wb") as file:
            file.write(image_bytes)
    
    #Эта функция обрабатывает нажатие кнопки Скачать фото
    def parse_func(self):
        
        options = webdriver.ChromeOptions()
        useragent = UserAgent()
        #Представимся useragent-ом как браузер IE
        options.add_argument(f"user-agent = {useragent.ie}")
        options.headless = True
        driver = webdriver.Chrome(executable_path="D:\\python\\chromedriver\\chromedriver.exe",options = options)
        
        
        
        self.user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
        #Создадим диалог для открытия файл со ссылками на лоты
        fname = QFileDialog.getOpenFileName(self.centralwidget, 'Open file')[0]
        #очистим текстовое поле для ведения лога
        self.textEdit.clear()
        self.textEdit.append('Будет открыт файл: ' + fname)
        #откроем файл для чтения
        f = open(fname, 'r')
        #создадим пустой список ссылок и считаем в него из файла ссылки на лоты
        links = []
        links = f.read().split(sep='\n')
        # links = f.read()
        #Пытаемся создать директорию имя которой содержит поисковый запрос
        # try:
        #     os.mkdir(os.path.basename(f"D:\\python\\coins_parser\\pictures_dataset\\{fname}" +'_set'))
        # #Если такая директория уже существует, выведем об этом сообщение в текстовое поле
        # except FileExistsError:
        #     self.textEdit.append('Каталог ' + fname+'_set' + ' уже существует')
        # В этом цикле мы будем парсить фотки лотов с каждой страницы с лотом
        for link in links:
            #пауза на случайное число секунд от 0 до 5
            sleep(randrange(5))
            driver.get(url=link)

            #Находим ссылки на картинки с лотом
            img = driver.find_elements_by_class_name("fotorama__img")
            
            #В этом цикле загружаем содержимое каждой картинки в виде байтов и вызываем функцию save_func для сохранения их в файлы картинок на диске
            for e,i in enumerate(img):
                #получаем полуный путь к картинке методом get_attribute из ранее полученного теха img, запрашиваем содержимое атрибута src
                src = i.get_attribute('src')
                #переменная dir_name будет содержать полный путь к ДИРЕКТОРИИ файла методом стрип обрезаем лишние символы расширения файла .txt
                #И передаём эту переменную в функцию сохранения файал на диск save_func
                dir_name = f"D:\python\coins_parser\pictures_dataset\{os.path.basename(fname)}".strip(".txt")
                print(src)
                image_bytes = bytes(requests.get(src).content)
                self.save_func(dir_name, str(src), image_bytes)
            
            
            # for i in range (1, 4):
            #     try:
            #         page = requests.get(link +'#i', headers = self.user_agent)
            #     except ConnectionError:
            #         self.textEdit.append("Отсутсвует соединение с интернетом")
            #     if page.status_code == 200:
            #         # print(page.status_code)
            #         html = BS(page.text, 'html.parser')
            #         foto_link = html.findAll('div', class_='fotorama__nav__frame fotorama__nav__frame--thumb')
            #         for foto in foto_link:
            #             src = foto.findAll('img', class_='fotorama__img')
            #             print(src)
            #     else:
            #         print(page.status_code)
            
            # print(link)
        #print(self.lots_links)
    #Эта функция будет принимать ссылки на страницу с пагинацией лотов и возвращать в ответ массив со ссылками на лоты с каждой страницы
    #Выводить в текстбокс общее количество наденных лотов, сохранять ссылки на них в файл и показывать путь к файлу в текстбоксе    
    #def paginator_lister(self, page_link, count):
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
