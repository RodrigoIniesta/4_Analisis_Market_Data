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

#print("First code")

#simulating random variables
nb_sims=10**6
df=5
lam=2
dist_name= 'normal'
dist_type = 'sim RV'

if dist_name == 'normal':
    x=np.random.standard_normal(nb_sims)
    x_desc= dist_type + ' ' + dist_name
elif dist_name == 'exponential':
    x=np.random.exponential(lam,nb_sims)
    x_desc= dist_type + ' ' + dist_name
elif dist_name == 'uniform':
    x=np.random.uniform(0,2,nb_sims)
    x_desc= dist_type + ' ' + dist_name
elif dist_name == 'student':
    x=np.random.standard_t(df,nb_sims)
    x_desc= dist_type + ' ' + dist_name+' | df='+str(df) 
elif dist_name == 'chi-squared':
    x=np.random.standard_t(df,nb_sims)
    x_desc= dist_type + ' ' + dist_name+' | df='+str(df)

'''
Todays goal - Create Jarque - Bera normality test
'''
x_variance=np.var(x)
x_skew = skew(x)
x_kurtosis = kurtosis(x) #Esta Kurtosis ya esta en exceso (K-3)
x_jarque_bera = nb_sims/6*(x_skew**2+1/4*x_kurtosis**2)
p_value = 1 - chi2.cdf(x_jarque_bera,df=2)
x_is_normal = (p_value>0.05)  #para revisar si el p_value es mayor 1-.95

#jb_list = [] #create a list
#jb_list.append(x_jarque_bera) #Para ir apilando los resultados correr varias veces

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


