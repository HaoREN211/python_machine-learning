# -*- coding: utf-8 -*-
# !/usr/bin/python
# python 3.6

import pandas as pd
from numpy import asmatrix
file_name = 'C.test_data201803.csv'
data = pd.read_csv(file_name)
data = asmatrix(data)
print(data[:, 1])
