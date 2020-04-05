# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

class DataFile:
    
    def __init__(self, dataFile, variable):
        self.dataFile = dataFile
        self.variable = variable
        
    def dataSeries(self):
        self.dataFile = pd.read_csv(self.dataFile , delimiter = "\t", header='infer')
        self.dataFile = self.dataFile[self.variable]
        self.dataFile = (self.dataFile).values
    
    def display(self):
        plt.figure(figsize = (15,5))
        plt.plot (self.dataFile)
        plt.ylabel('Global Horizontal Irradiance (W/m2)')
        plt.xlabel('Hours')
        plt.xlim(0, 17520)
        plt.ylim(0, 1000)
        plt.show()
        


class PrepareData (DataFile):
    
    history = input("history?: ")
    history = int(history)
    horizon = input("horizon?: ")
    horizon = int(history)  
    
    def __init__(self, dataFile, variable):
        super().__init__(dataFile, variable)
        self.column = []
   
    
    def scaler(self):
        self.dataFile = (self.dataFile).reshape((-1, 1))
        scaler = MinMaxScaler()
        scaled = (scaler).fit_transform(self.dataFile)
        self.dataFile = pd.DataFrame(scaled)
 
    def inputOutput (self, dropnan = True):
    
        for i in range(PrepareData.history, 0, -1):
            (self.column).append((self.dataFile).shift(i))
        
        for i in range(0, PrepareData.horizon):
            (self.column).append((self.dataFile).shift(-i)) 
        
        self.dataFile = pd.concat((self.column), axis=1)
        self.dataFile = pd.DataFrame(np.vstack([(self.dataFile).columns, (self.dataFile)]))
        #self.dataFile = np.array (self.dataFile)
        #self.dataFile = self.dataFile[~np.isnan(self.dataFile).any(axis=1)]
        if dropnan:
            self.dataFile.dropna(inplace=True)
            
        self.dataFile = self.dataFile.values
        X, y =  self.dataFile[:, :PrepareData.history], self.dataFile[:, PrepareData.history:]
        
        return np.array(X), np.array(y)
 


#data = PrepareData (directory, 'dw_solar')




   
    

