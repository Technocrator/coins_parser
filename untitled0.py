# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 13:19:38 2022

@author: 0
"""

import os

f =os.walk(f"D:\python\coins_parser\pictures_dataset\cler_test_set")

for root, dirs, files in f:
    for file in files:
        print(file)