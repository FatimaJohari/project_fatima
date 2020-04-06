# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense



from .preparation import PrepareData

class Forecasting:
    # path to the input file of solar radiation
    directory = input("file directory?: ") #"C:/Users/fatjo876/Documents/Year_2/PhD Courses/forecasting/sxf_2015-2016.txt"
    variable = input ("on which coulmn you would like to have forecasting?")
    variable = str(variable)
    history = input("from how many hours to the past you would like to predict the future?")
    history = int(history)
    horizon = input ("how many hours to the the future is going to be predicted?")
    horizon = int(horizon)
    
    
    def __init__(self):
        data = PrepareData(Forecasting.directory, Forecasting.variable,Forecasting.history,Forecasting.horizon)
        self.X , self.y = data.inputOutput(self)
        
     
    def trainTest (self):
        
        trainSize = int(len(self.X) * 0.5)

        train_X , train_y = self.X[1:trainSize] , self.y[1:trainSize]
        test_X, test_y = self.X[trainSize:], self.y[trainSize:]
        train_X = train_X.reshape((train_X.shape[0], train_X.shape[1], 1))
        test_X = test_X.reshape((test_X.shape[0], test_X.shape[1], 1))
        
        return train_X, test_X, train_y, test_y
    
    def forecasting (self):
        self.train_X, self.test_X, self.train_y, self.test_y = Forecasting.trainTest(self)
        
        model = Sequential()
        model.add(LSTM(2, activation='relu', return_sequences=True, 
                       input_shape=(Forecasting.history, 1)))
        model.add(LSTM(2, activation = 'relu'))
        model.add(Dense(Forecasting.horizon))
        #model.add(Dropout(0.4))
        model.compile(optimizer='adam', loss='mae', metrics=['accuracy'])

        # fit network
        history = model.fit(self.train_X, self.train_y,
                            epochs=10, batch_size= 1, 
                            validation_data=(self.test_X, self.test_y),
                            verbose=0)
        return history

    
    def display (self):
        # summarize history for accuracy
        plt.figure()
        plt.plot((Forecasting.forecasting(self)).history['accuracy'],'blue')
        plt.plot((Forecasting.forecasting(self)).history['val_accuracy'],'green')
        plt.title('model accuracy')
        plt.ylabel('accuracy')
        plt.xlabel('epoch')
        plt.legend(['train', 'test'], loc='upper left')
        plt.show()

