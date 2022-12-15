# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 16:41:09 2022

@author: 0
"""

import requests
from bs4 import BeautifulSoup as BS

user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

r = requests.get("https://auction.ru", headers = user_agent)
print(r.content)
html = BS(r.content, 'html.parser')