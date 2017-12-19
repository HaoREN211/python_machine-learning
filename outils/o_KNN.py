# -*- coding: utf-8 -*-
#!/usr/bin/python
# K最近邻(kNN，k-NearestNeighbor)分类算法

from numpy import *;
import  operator;

def createDataSet() :
    groupe = array([[1.0, 1.1],[1.0, 1.0],[0, 0],[0, 0.1]]);
    labels = ['A', 'A', 'B', 'B'];
    return groupe, labels;



def classify0(inX, dataset, labels, k):
    #nombre de enregistrement
    #计算行数   .
    datasetsize = dataset.shape[0];

    # 两矩阵差值
    #difference de chaque attribut
    diffmat = tile(inX, (datasetsize, 1)) -dataset;

    #carre de chaque attribut.
    # 矩阵内各元素平方
    sqdiffmat = diffmat**2;

    #calcul par chaque ligne
    # 计算矩阵各行之和，得到一个N X 1矩阵
    sqdistances = sqdiffmat.sum(axis=1);

    #calcul de distance entre le point a tester avec les points d'apprentissage
    # 计算得到的新矩阵各元素开方值，就是训练集各点和测试点的距离差
    distances = sqdistances**0.5;

    #recuperer la liste de indice d'ordre de distance en ordre croissant de chaque point apprentissage
    # 按照距离差大小重新排列
    sortdistanceindicies = distances.argsort();
    classc_count = {};

    #calculer le nombre de libelle de k premier point
    for i in range(k):
        vote_labels = labels[sortdistanceindicies[i]];
        classc_count[vote_labels]=classc_count.get(vote_labels, 0)+1;
    sorted_class_count = sorted(classc_count.iteritems(),
                                key=operator.itemgetter(1),
                                reverse=True);
    return sorted_class_count[0][0];



def dating_calss_test_knn():
    """
    用约会网站上的数据对knn进行验证
    :return: 将答案显示在终端上
    """