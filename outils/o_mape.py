# -*- coding: utf-8 -*-
# !/usr/bin/python
# python 3.6

from numpy import asarray, abs

# Mean Absolute Percentage Error
def cal_mape(y_real, y_pred):
    y_real = asarray(y_real)
    y_pred = asarray(y_pred)
    y_real_length = len(y_real)
    y_real_pred_length = len(y_pred)

    error = 0
    index = 0

    if y_real_length == y_real_pred_length:
        for i in range(index):
            error += abs((y_real[index]-y_pred[index])*0.1/y_real[index])
        error = error/y_real_length

    return error