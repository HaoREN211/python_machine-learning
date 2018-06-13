#!/usr/bin/python
# -*- coding: utf-8 -*-
# K最近邻(kNN，k-NearestNeighbor)分类算法

from numpy import *;
import  operator;
from  o_transfer_file_to_matrix import  file_2_matrix;
from o_normalize import  auto_norm;
from os import listdir;
from outils.o_img_2_vector import img_2_vector;

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



def dating_calss_test_knn(k):
    """
    用约会网站上的数据对knn进行验证
    :param k: k 近邻
    :return: 将答案显示在终端上
    """
    ratio_data_test = 0.1; # 测试集数据比例
    groupe, libelles = file_2_matrix("./donnees/d_datingTestSet2.txt", 3);
    dataset, decalage, max_value, min_value = auto_norm(groupe); # 将数据归一化
    nombre_ligne = dataset.shape[0];
    nombre_data_test = int(nombre_ligne*ratio_data_test); # 测试集数据量
    nombre_erreur = 0.0; # 分类器出错总数
    print  nombre_data_test;

    """
    将数据集前nombre_data_test的数据当成测试数据 并一一循环
    比较分类器对测试集给出的分类和测试集原应归属的分类
    """
    for i in range(nombre_data_test):
        resultat = classify0(dataset[i, :],
                             dataset[nombre_data_test:nombre_ligne, :],
                             libelles[nombre_data_test:nombre_ligne],
                             k);
        print "the classifier came back with: %d, the real answer is: %d" % (resultat, libelles[i]);
        if (resultat != libelles[i]):
            nombre_erreur +=1.0;

    print "the total error rate is : %f" % (float(nombre_erreur)/float(nombre_data_test));
    return int((float(1)-(float(nombre_erreur)/float(nombre_data_test)))*int(100));


def classify_person():
    """
    给定一个人的信息 来判断他是否是海伦喜欢的类型
    :return:
    """

    groupe, libelles = file_2_matrix("./donnees/d_datingTestSet2.txt", 3);
    dataset, decalage, max_value, min_value = auto_norm(groupe);
    distance_avion = float(raw_input("每年坐飞机飞行了多少距离？"));
    resultat_libelle = ["不适合你","可能适合你","极大可能适合你"];
    pourcentage_game = float(raw_input("玩游戏占了生活时间多少比重?"));
    litre_glace = float(raw_input("每年吃了升冰淇淋?"));
    input_list = array([distance_avion, pourcentage_game, litre_glace]); # 归一化输入数据
    resultat = classify0((input_list-min_value)/decalage, dataset, libelles, 3);
    print "这哥们", resultat_libelle[resultat-1];


0