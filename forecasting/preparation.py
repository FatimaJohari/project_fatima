# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

class DataFile:
    """
    The input file directory imported as csv, 
    the desired column is read and illustrated
    """
    
    def __init__(self, dataFile, variable):
        self.dataFile = dataFile
        self.variable = variable
        
    def dataSeries(self):
        self.dataFile = pd.read_csv(self.dataFile , delimiter = "\t", header='infer')
        self.dataFile = self.dataFile[self.variable]
        return (self.dataFile).values
    
    def display(self):
        plt.figure(figsize = (15,5))
        plt.plot (self.dataFile)
        plt.ylabel('Global Horizontal Irradiance (W/m2)')
        plt.xlabel('Hours')
        plt.xlim(0, 17520)
        plt.ylim(0, 1000)
        plt.show()
        


class PrepareData (DataFile):
    """
    the time series is modified to have inputs (X) and outputs (y)
    """
    # ask for the length of past time steps to be kept by the memory and
    # the future time step  to be predicted. 
    #history = input("history?: ")
    #history = int(history)
    #horizon = input("horizon?: ")
    #horizon = int(history)  
    
    def __init__(self, dataFile, variable, history , horizon):
        super().__init__(dataFile, variable)
        self.history = history
        self.horizon = horizon
        self.column = []
       
    def scaler(self):
        " Normalization function"
        
        self.dataFile = (DataFile.dataSeries(self)).reshape((-1, 1))
        scaler = MinMaxScaler()
        scaled = (scaler).fit_transform(self.dataFile)
        return pd.DataFrame(scaled)

    def inputOutput (self, dropnan = True):
        self.dataFile = PrepareData.scaler(self)
        #get t-n time steps into the past (history)
        for i in range(self.history, 0, -1):
            (self.column).append(self.dataFile.shift(i))
        
        #get t+n time steprs into the future (horizon)
        for i in range(0, self.horizon):
            (self.column).append(self.dataFile.shift(-i)) 
        
        # concat the columns from t-n and t+n time steps in one dataframe
        self.dataFile = pd.concat((self.column), axis=1)
        
        # reindex the dataframe
        self.dataFile = pd.DataFrame(np.vstack([(self.dataFile).columns, (self.dataFile)]))
        
        # remove rows with nan
        if dropnan:
            self.dataFile.dropna(inplace=True)
        
        # seperate the data into input and output X and y
        self.dataFile = self.dataFile.values
        X, y =  self.dataFile[:, :self.history], self.dataFile[:, self.history:]
        
        return np.array(X), np.array(y)
    
  
   

