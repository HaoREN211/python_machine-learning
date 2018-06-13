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
X = data['time']
Y = data['KWH']
print(data.head())
print(data.dtypes)



# verify missing data
# missingno.matrix(data)

data = pd.read_csv(file_name, parse_dates=[1], index_col='time')
time_series = data['KWH']
X_train, X_val, y_train, y_val = train_test_split(X, Y,
                                                  test_size=0.1)
test_set = [(X_val, y_val)]
# specify parameters via map
params = {
    'learning_rate': 0.05,
    'n_estimators': 100,
    'subsample': 0.6,
    'colsample_bytree': 0.6,
    'max_depth': 7,
    'min_child_weight': 1,
    'reg_alpha': 2,
    'gamma': 0
}
regressor = xgb.XGBRegressor(learning_rate=params['learning_rate'],
                             n_estimators=params['n_estimators'],
                             booster='gbtree',
                             objective='reg:linear',
                             n_jobs=-1,
                             subsample=params['subsample'],
                             colsample_bytree=params['colsample_bytree'],
                             random_state=0,
                             max_depth=params['max_depth'],
                             gamma=params['gamma'],
                             min_child_weight=params['min_child_weight'],
                             reg_alpha=params['reg_alpha'])
regressor.fit(X_train,
              y_train,
              verbose=True,
              early_stopping_rounds=10,
              eval_metric=y_val,
              eval_set=X_val)
# num_round = 2
# bst = xgb.train(params, time_series, num_round)
# make prediction
# preds = bst.predict(X_val)
# print('prediction: ')
# print(preds)
