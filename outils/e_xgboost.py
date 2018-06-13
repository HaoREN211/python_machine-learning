# -*- coding: utf-8 -*-
# !/usr/bin/python
# python 3.6

import pandas as pd
from numpy import asmatrix
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from numpy import abs, mean
import scipy.stats as st
import outils.o_mape as mape

# 读取文件
file_name = 'C.test_data201803.csv'
data = pd.read_csv(file_name)
Y = data['KWH']

print('real y values: ')
print(Y)

data = asmatrix(data)
X = data[:, 0]
print(X)


# 划分训练集和测试集
seed = 7
test_size = 0.1
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    Y,
                                                    test_size=test_size,
                                                    random_state=seed)

X_train = asmatrix(X_train)


# 建立模型
model = XGBClassifier()
model.fit(X_train, y_train)


# 预测
y_pred = model.predict(X)
mape = mape.cal_mape(Y, y_pred)

print('prediction of y')
print(y_pred)
print('Mean Absolute Percentage Error')
print(mape)

# 通过交叉验证寻找最优参数并且优化模型
params = {"n_estimators": st.randint(100, 500),
          'max_depth': st.randint(6, 30)}
model_updated = RandomizedSearchCV(
    model, params, cv=10, random_state=1, n_iter=20)
model_updated.fit(X_train, y_train)

# 预测
y_pred_update = model_updated.predict(X)
mape_update = mape.cal_mape(Y, y_pred_update)

print('prediction updated of y')
print(y_pred_update)
print('Mean Absolute Percentage Error')
print(mape_update)
