import
import os

#каталог с набором данных

data_dir = 'D:\\python\\coins_parser\\pictures_dataset\\10_kop_silver_sorted'
#каталог с даными для обучения
train_dir = 'train'
#каталог с данными для проверки
val_dir = 'val'
#Каталог с данными для тестирования
test_dir = 'test'

#часть набора данных для тестирования
test_data_portion = 0.15
#Часть набора данных для проверки
val_data_portion = 0.15
#Количество элементов данных в одном классе
nb_images = 5227
# Функция создания каталога с двумя подкаталогами: coins и not_coins

def create_directory(dir_name):
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
    os.makedirs(dir_name)
    os.makedirs(os.path.join(dir_name, "coins")))
    os.makedirs(os.path.join(dir_name, "not_coins"))

#Функция копирования изображений в заданный каталог.

def copy_images(start_index, end_index, source_dir, dest_dir):
    for i in range(start_index, end_index):
        shutil.copy2(os.path.join(source_dir, "coin." + str(i) + ".jpg"),
                     os.path.join(dest_dir, "coins"))
        shutil.copy2(os.path.join(source_dir, "not_coin." + str(i) + ".jpg"),
                     os.path.join(dest_dir, "not_coins"))

