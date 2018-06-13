# -*- coding: utf-8 -*-
#!/usr/bin/python
# Python3.6

from numpy import asmatrix, mean, cov, argsort
from numpy.linalg import eig

# PCA 主成分分析 Principal Component Analysis
# 降维的主要作用为
# 1.使得数据集更容易使用
# 2.降低很多算法的计算开销
# 3.去除噪音
# 4.使结果更加通俗易懂


def load_data_set(file_name, delimiter='\t'):
    """
    读取file_name文件里的数据并将其转化为float类型
    :param file_name:
    :param delimiter:
    :return:
    """
    file = open(file_name)
    string_array = [line.strip().split(delimiter)
                    for line in file.readlines()]
    data_array = [map(float, line) for line in string_array]
    return asmatrix(data_array)


def pca(data_mat, top_n_feat=9999999):
    # 去除平均值后求协方差矩阵
    mean_values = mean(data_mat, axis=0)
    data_without_mean = data_mat - mean_values
    cov_mat = cov(data_without_mean, rowvar=0)

    # 求特征值和特征向量
    eig_values, eig_vectors = eig(asmatrix(cov_mat))

    # 将特征值进行排序 并将特征值从大到小的下标返回
    # 并返回头top_n_feat大的特征值和特征向量
    eig_values_sorted = argsort(eig_values)
    eig_values_sorted_filtered = eig_values_sorted[: -(top_n_feat+1): -1]
    eig_vectors = eig_vectors[:, eig_values_sorted_filtered]

    # 将原数据集投影在主成分坐标轴上
    # 拉伸 + 改变方向
    new_mat = data_without_mean * eig_vectors
    final_mat = (new_mat * eig_vectors.T) + mean_values
    return new_mat, final_mat