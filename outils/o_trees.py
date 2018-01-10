# -*- coding: utf-8 -*-
#!/usr/bin/python

from math import log;

def diff_append_extend():
    a=[1,2,3];
    b=[4,5,6];
    print  "a:";
    print a;
    print "b:";
    print b;
    print "a append b:";
    a.append(b);
    print a;
    a = [1, 2, 3];
    print "a extend b:";
    a.extend(b);
    print a;

def calcShannonEnt(data_set):
    """
    计算给定数据集的香农熵
    :param dataSet: 输入数据集
    :return: 给定数据集的香农熵
    """
    """
    划分数据集的大原则是：将无序的数据变得更加有序。
    在划分数据集之前之后信息发生的变化称为信息增益。
    集合信息的度量方式称为香农熵或者简称为熵
    """
    taille_data_set = len(data_set);
    compte_libelle = {};
    for ligne in data_set:
        """
        统计每个类别在数据集出现的次数
        """
        libelle_courant = ligne[-1];
        if libelle_courant not in compte_libelle.keys():
            compte_libelle[libelle_courant] = 0;
        compte_libelle[libelle_courant] += 1;
    shannonEnt = float(0.0);
    for key in compte_libelle:
        probabilite = float(float(compte_libelle[key])/float(taille_data_set));
        shannonEnt -= probabilite * float(log(probabilite,2));
    return shannonEnt;


def creer_dataset():
    """
    创建一个检测香农熵计算的数据集
    :return:
    """
    dataset = [
        [1,1,'yes'],
        [1, 1, 'yes'],
        [1,0,'no'],
        [0,1,'no'],
        [0,0,'no']
    ];
    libelle = ['no surfacing','flippers'];
    return dataset, libelle;



def splitDataset(dataset, axis, value):
    """
    按照给定特征划分数据集
    :param dataset:
    :param axis:
    :param value:
    :return:
    """
    """
    当axis代表的特征值等于value时
    返回由除axis特征的其他特征和类别的矩阵
    用来计算按照当前特征值建造决策树分支所包含的香农熵
    """
    ret_dataset = [];
    for ligne in dataset:
        if ligne[axis] == value:
            reduced_ligne = ligne[:axis];
            reduced_ligne.extend(ligne[axis+1:]);
            ret_dataset.append(reduced_ligne);
    return ret_dataset;