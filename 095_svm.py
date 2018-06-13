# -*- coding: utf-8 -*-
# !/usr/bin/python

import outils.o_svm as svm_outil
from numpy import matrix as mat
from numpy import zeros
from numpy import multiply


file_name = 'donnees/svm/testSet.txt'
data_arr, label_arr = svm_outil.load_data_set(file_name)
b, alphas = svm_outil.smoSimple(data_arr, label_arr, 0.6, 0.001, 40)
print(label_arr)
print("b: ")
print(b)
print("alphas")
print(alphas)
"""
m = 6
alpha = mat([6, 6, 6])
test = mat([1, 2, 3]).T
print(alpha)
print(test)
print(multiply(alpha, test))
"""