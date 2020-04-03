# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

class DataFile:

    def __init__(self, dataFile, variable):
        self.dataFile = dataFile
        self.variable = variable
        
    def dataSeries(self):
        self.dataFile = pd.read_csv(self.dataFile , delimiter = "\t", header='infer')
        self.dataFile = self.dataFile[self.variable]
        return (self.dataFile).values
    
directory = "C:/Users/fatjo876/Documents/Year_2/PhD Courses/AdvancedSolarIrradianceTheory-master/sxf_2015-2016.txt"

data = DataFile(directory, 'dw_solar')
data.dataSeries()
plt.plot ()

class DataPrepare:
    
    def __init__(self, dataFile, history, horizon):
        super().__init__()
        self.dataFile = self.dataFile
        self.horizon = horizon
        self.history = history
    
    def scaler(self):
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        self.scaled = pd.DataFrame((self.scaler).fit_transform(self.dataFile))
        
    def prepareData (self, dataFile, history, horizon, dropnan=True):

        cols= []
    
        for i in range(self, history, 0, -1):
            cols.append(data.shift(i))
        
        for i in range(0, horizon):
            cols.append(data.shift(-i)) 
        
        dataframe = pd.concat(cols, axis=1)
    
        values = pd.DataFrame(np.vstack([data.columns, data]))
    
        if dropnan:
            dataframe.dropna(inplace=True)
    

        dataframe = dataframe.values
        X, y =  dataframe[:, :history], dataframe[:, history:]

        return np.array(X),np.array(y)
    
    
    
test = DataFile ('hell', 'tets')

print (test.dataFile)    
directory = "C:/Users/fatjo876/Documents/Year_2/PhD Courses/AdvancedSolarIrradianceTheory-master/sxf_2015-2016.txt"

data = DataFile(directory, 'dw_solar')
data
