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



def choisir_meilleur_attribut_a_decouper(dataset):
    """
    选择最好的数据集划分方式
    :param dataset: 输入数据集
    :return:
    """
    """
    计算每个特征所具有的香农熵。
    计算方式是迭代每个特征，然后通过迭代每个特征的所有可能的值所具有的总和。
    信息增益为初始数据集所具有的香农熵减去每个特征的香农熵。
    信息增益是熵的减少或者是数据无序度的减少。
    也就是说每个特征的香农熵越低越好。
    """

    # 计算特征数量 也就是数据集的列数。
    nombre_attribut = len(dataset[0])-1;

    # 计算数据集的初始香农熵。
    entropy_base = calcShannonEnt(dataset);

    # 假使初始的信息增益为0。
    best_info_gain = 0.0;

    # 初始最优特征为-1.
    best_attribut = -1;

    for i in range(nombre_attribut):
        """
        迭代每个特征 计算每个特征的香农熵总和已经信息增益。
        使用列表推导来创建新的列表，
        将数据集中所有第i个特征值或者所有可能存在的值写入这个新list中。
        """

        # 提取第i列，也就是第i个特征的所有可能值
        liste_attribut = [exemple[i] for exemple in dataset];

        # 提取不重复的i特征的所有可能的值 set是用来建立无序不重复元素集
        unique_val = set(liste_attribut);

        # 初始新的信息量
        nouveau_entropy = float(0.0);
        for value in unique_val:
            """
            遍历当前特征中的所有唯一属性值，
            对每一个唯一属性值划分一次数据集，
            然后计算数据集的新熵值，
            并对所有唯一特征值得到的熵求和。
            """
            # 得到除去i特征且i特征值为value的初始数据集子集
            sub_dataset = splitDataset(dataset, i, value);

            # 计算i特征的value值出现的可能值
            probabilite = float(float(len(sub_dataset))/float(len(dataset)));

            # 计算i特征的value值所包含的信息量
            entropy_tmp = calcShannonEnt(sub_dataset);

            # 累加i特征的信息量
            nouveau_entropy += float(float(probabilite)*float(entropy_tmp));

        # 计算信息增量
        info_gain = entropy_base - nouveau_entropy;
        if(info_gain > best_info_gain):
            """
            信息增益是熵的减少或者是数据无序度的减少
            """
            best_info_gain = info_gain;
            best_attribut = i;
    return best_attribut;