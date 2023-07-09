# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 23:56:40 2021

@author: MRDV
"""

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy
import importlib
from scipy.stats import skew,kurtosis,chi2



#### get market data ####
file='BBVA.MC'
#file='^VIX'
#file='MXN=X'
path = 'C:\\Users\\rodrigo\\Documents\\Finanzas Cuantitativas con Python\\4_Analisis_Market_Data\\'+file+'.csv'
raw_data = pd.read_csv(path)
#x = raw_data['Close'] #Formato Series (indice mas valores)
x = raw_data['Close'].values #Formato arreglo de valores (solo valores)
#data_lenght=len(x) #obtener la longitud del vectos = cantidad de datos
data_lenght=raw_data.shape [0] #longitud desde las caracteristicas del arreglo

###Create returns of the series in another file###
t = pd.DataFrame()
#t['date']=raw_data['Date']
#type(t['date'][0]) #checking the data type
t['date'] = pd.to_datetime(raw_data['Date'],dayfirst=True) #convert the data type to date instead of string
t['close'] = raw_data['Close']
t.sort_values(by='date',ascending = True)
for i in range(data_lenght-1):
    if pd.isna(t['close'][i]): #Check if the data is nan y fill it withe last one
        t['close'][i]=t['close'][i-1]
t['close_shift_1'] = t['close'].shift(1) #create a column with the shifted data by row
t['return']=t['close']/t['close_shift_1']-1 
t=t.dropna() #erase row that have nan
t=t.reset_index(drop=True) #to reste the index of the table as we erase some lines
x=t['return'].values

##JarqueVera###
x_variance=np.var(x) 
x_skew = skew(x)
x_kurtosis = kurtosis(x) #Esta Kurtosis ya esta en exceso (K-3)
x_jarque_bera = data_lenght/6*(x_skew**2+1/4*x_kurtosis**2)
p_value = 1 - chi2.cdf(x_jarque_bera,df=2)
x_is_normal = (p_value>0.05)  #para revisar si el p_value es mayor 1-.95

#jb_list = [] #create a list
#jb_list.append(x_jarque_bera) #Para ir apilando los resultados correr varias veces
x_desc = 'market data ' +  file
print('kurtosis is ' + str(x_kurtosis)) 
print('skew is ' + str(x_skew))
print('Jarque-Bera statistic is ' + str(x_jarque_bera))
print('p-value is :' + str(p_value))
print('is normal ' + str(x_is_normal))
#plot histograms (run all at time)
plt.figure()
plt.hist(x,bins=100)
plt.title(x_desc)
plt.show()


