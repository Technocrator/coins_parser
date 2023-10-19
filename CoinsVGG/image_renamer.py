# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 15:16:00 2023

@author: 0
"""

from imutils import paths
import numpy as np
import random
import os

print ("[INFO] Renaming images..." )

#Укажим путь к какталогу, который содержит подкаталоги с картинками
path = "D:\\python\\coins_parser\\pictures_dataset\\10_kop_silver_sorted\\train"

#Считаем список поддерикторий с картинками
image_dir = sorted(list(os.listdir(path)))
print(image_dir)

#Запустим цикл переименования файлов
for directory in image_dir:
    image_name = sorted(list(os.listdir(path+"\\"+directory)))
    print(image_name)
    for i, name in enumerate(image_name):
        os.rename(path+"\\"+directory+"\\"+name, path+"\\"+directory+"\\"+f"{directory}"+str(i)+".jpg")
    