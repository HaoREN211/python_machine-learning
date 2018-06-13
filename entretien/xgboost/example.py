# -*- coding: utf-8 -*-
# !/usr/bin/python
# python 3.6

import xgboost as xgb
import numpy as np
from sklearn.model_selection import KFold, train_test_split, GridSearchCV
from sklearn.metrics import confusion_matrix, mean_squared_error
from sklearn.datasets import load_iris, load_digits, load_boston

# 用Xgboost建模，用sklearn做评估
# 二分类问题，用混淆矩阵

digits = load_digits()
y = digits['target']
X = digits['data']


# K折的切分器
kf = KFold(n_splits=2, shuffle=True, random_state=1234)
for train_index, test_index in kf.split(X):
    xgboost_model = xgb.XGBClassifier().fit(X[train_index], y[train_index])
    # 预测结果
    pred = xgboost_model.predict(X[test_index])
    # 标准答案
    ground_truth = y[test_index]
    print(confusion_matrix(ground_truth, pred))



# 多分类
iris = load_iris()
y_iris = iris['target']
X_iris = iris['data']
kf = KFold(n_splits=2, shuffle=True, random_state=1234)
for train_index, test_index in kf.split(X_iris):
    xgboost_model = xgb.XGBClassifier().fit(X_iris[train_index], y_iris[train_index])
    # 预测结果
    pred = xgboost_model.predict(X_iris[test_index])
    # 标准答案
    ground_truth = y_iris[test_index]
    print(confusion_matrix(ground_truth, pred))

# 回归问题
boston = load_boston()
y_boston = boston['target']
X_boston = boston['data']
kf = KFold(n_splits=2, shuffle=True, random_state=1234)
for train_index, test_index in kf.split(X_boston):
    xgboost_model = xgb.XGBRegressor().fit(X_boston[train_index], y_boston[train_index])
    # 预测结果
    pred = xgboost_model.predict(X_boston[test_index])
    # 标准答案
    ground_truth = y_boston[test_index]
    print(mean_squared_error(ground_truth, pred))


boston = load_boston()
y_boston = boston['target']
X_boston = boston['data']
xgb_model = xgb.XGBRegressor()
# 参数字典
param_dict = {'max_depth': [2, 4, 6], 'n_estimators': [50, 100, 200]}

rgs = GridSearchCV(xgb_model, param_dict)

rgs.fit(X_boston, y_boston)

print(rgs.best_score_)

print(rgs.best_params_)
