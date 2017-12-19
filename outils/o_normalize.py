# -*- coding: utf-8 -*-
#!/usr/bin/python

from numpy import zeros, shape, tile;

def auto_norm(dataset):
    """
    Normalize the dataset to the range 0...1
    :param dataset: the input dataset
    :return: 1. a normalized dataset, 2. the range, 3. the max value, 4.the min value
    """
    min_valeur = dataset.min(0); # 找出每列中数值最小的数
    max_valeur = dataset.max(0); # 找出每列中数值最大的数
    decalage = max_valeur - min_valeur; #找出每列中数值最大与最小的差值 即range
    norm_dataset = zeros(shape(dataset)); #初始化结果矩阵
    nombre_ligne = dataset.shape(0); # 找出dataset的列数
    norm_dataset = dataset - tile(min_valeur, (nombre_ligne, 1)); # 矩阵各个元素减去所在列的最小值
    norm_dataset = norm_dataset/tile(decalage, (nombre_ligne, 1)); # 矩阵各个元素除以所在列的range
    return norm_dataset, decalage, max_valeur, min_valeur;