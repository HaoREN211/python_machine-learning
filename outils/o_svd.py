# -*- coding: utf-8 -*-
#!/usr/bin/python

# SVD 奇异值分解 Singular Value Decomposition
# 大体思想是对特征进行分组从而达到降维的目的

# 和在UTC学习的矩阵奇异值是同一个东西
# 假设原数据集为D，维度为 (m, n)
# 那么它可以表示为三个矩阵的乘 D = U * I * V
# U = (m, m), I = (m, n), V = (n, n) 其中I只有从大到小排列的对角元素
# 而且 I 中会有r个不为零的奇异值 r <= m, r <= n

from numpy import asmatrix
from numpy.linalg import svd

# 直接实现SVD例子
dataset = asmatrix()
svd(dataset)



