# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 13:19:10 2022

@author: 0
"""

import selenium
from selenium import webdriver
from fake_useragent import UserAgent

options = webdriver.ChromeOptions()
useragent = UserAgent()

options.add_argument(f"user-agent = {useragent.ie}")

url = "https://auction.ru/offer/rubl_1896_ag_porezhe_khoroshee_sostojanie_xf_fotr868-i232199685991760.html"

driver = webdriver.Chrome(executable_path="D:\\python\\chromedriver\\chromedriver.exe",options = options)
driver.get(url=url)