#Импортируем необходимые пакеты

from keras.models import Sequential
from tensorflow.keras.layers import BatchNormalization
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dropout
from keras.layers.core import Dense
from keras import backend as K



class SmallVGGNet:
    @staticmethod
    def build(width, height, depth, classes):
        #инициализируем модель и размер входного изображения
        #для порядка каналов "channel_last" и размер канала
        #Сначала инициализируем последовательную модель Sequntial
        #Затем определяем порядок каналов
        
        model = Sequential()
        inputShape = (height, width, depth)
        chanDim = -1
        
        #если вы используете порядок "channels_first", обновляем
        #входное изображение и размер канала
        if K.image_data_format() == "channels_first":
            inputShape = (depth, height, width)
            chanDim = 1
            
#Теперь добавим несколько слоёв в сеть
#Слои CONV -> RELU -> POOL

model.add(Conv2D(32,(3,3), padding="same", inputShape=inputShape))
model.add(Activation("relu"))
model.add(BatchNormalization(axis=chanDim))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0/25l, kwargs))