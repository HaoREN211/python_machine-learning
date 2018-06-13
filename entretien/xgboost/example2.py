# -*- coding: utf-8 -*-
# !/usr/bin/python
# python 3.6
# https://github.com/Jenniferz28/Time-Series-ARIMA-XGBOOST-RNN/blob/master/Gpower_Xgb_Main.py


import pandas as pd
import numpy
import matplotlib.pyplot as plt
import missingno
from sklearn.model_selection import train_test_split
import xgboost as xgb

# load data from csv file
file_name = 'C.test_data201803.csv'
data = pd.read_csv(file_name)
data.values
X = data['time']
Y = data['KWH']
print(data.head())
print(data.dtypes)



# verify missing data
# missingno.matrix(data)

data = pd.read_csv(file_name, parse_dates=[1], index_col='time')
time_series = data['KWH']
X_train, X_val, y_train, y_val = train_test_split(X, Y,
                                                  test_size=0.2)

print(numpy.shape(X_train))
print(numpy.shape(X_val))



# specify parameters via map
param = {'max_depth':2, 'eta':1, 'silent':1, 'objective':'binary:logistic' }
num_round = 2
bst = xgb.train(param, time_series, num_round)
# make prediction
preds = bst.predict(X_val)
print('prediction: ')
print(preds)
