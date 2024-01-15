# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 11:52:47 2024

@author: 0
"""
"""
Скрипт поиска геометрическхи фигур - окружностей на изображениях, с целью идентификации предметов похожих на монету :)

"""

%matplotlib inline
%config InlineBackend.figure_format = 'retina'

import cv2 as cv
import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
from pprint import pprint
