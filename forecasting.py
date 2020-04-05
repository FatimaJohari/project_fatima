# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Activation
from sklearn.preprocessing import MinMaxScaler

from .preparation import PrepareData

class Forecasting:
    
    def __init__(self, X,y ):
        self.X = PrepareData.X
        self.y = PrepareData.y
     
    def trainTest (self):
        
        trainSize = int(len(self.X) * 0.5)

        train_X , train_y = self.X[1:trainSize] , self.y[1:trainSize]
        test_X, test_y = self.X[trainSize:], self.y[trainSize:]
        train_X = train_X.reshape((train_X.shape[0], train_X.shape[1], 1))
        test_X = test_X.reshape((test_X.shape[0], test_X.shape[1], 1))
        
        return train_X, test_X, train_y, test_y
    
    def forecasting (self):
        model = Sequential()
        model.add(LSTM(2, activation='relu', return_sequences=True, input_shape=(PrepareData.history, 1)))
        model.add(LSTM(2, activation = 'relu'))
        model.add(Dense(PrepareData.horizon))
        model.add(Dropout(0.4))
        model.compile(optimizer='adam', loss='mae', metrics=['accuracy'])

        # fit network
        history = model.fit(train_X, train_y, epochs=20, batch_size= 1 , validation_data=(test_X, test_y), verbose=2)
        