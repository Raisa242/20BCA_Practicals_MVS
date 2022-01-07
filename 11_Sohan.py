# -*- coding: utf-8 -*-
"""
Created on

@author: Sohan Immanuel
"""

import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import FactorAnalysis
from sklearn import preprocessing
from sklearn.datasets import load_digits
os.chdir("C:/Users/Sumanth samuel/Desktop")
data=pd.read_csv('hotel_bookings.csv')
data.drop(['adr'],axis=1,inplace=True)
print(data.head())
print(data.dtypes)
print(data.shape)
print(data.head(15))
data.info()
X, _ = load_digits(return_X_y=True)
fa_Analysis = FactorAnalysis(n_components=6, random_state=80)
X_fa_Analysis  = fa_Analysis.fit_transform(X)
print(X_fa_Analysis.shape)