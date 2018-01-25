# -*- coding: utf-8 -*-
#!/usr/bin/python

from math import log;
from operator import itemgetter;
"""
itemgetter
operator模块提供的itemgetter函数用于获取对象的哪些维的数据，参数为一些序号（即需要获取的数据在对象中的序号），下面看例子。
a = [1,2,3] 
>>> b=operator.itemgetter(1)      //定义函数b，获取对象的第1个域的值
>>> b(a) 
2 

>>> b=operator.itemgetter(1,0)   //定义函数b，获取对象的第1个域和第0个的值
>>> b(a) 
(2, 1) 

要注意，operator.itemgetter函数获取的不是值，而是定义了一个函数，通过该函数作用到对象上才能获取值。
"""

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


def majority_cnt(classlist):
    """
    该函数使用分类名称的列表，然后创建键值classlist中唯一值的数据字典，
    字典对象存储了classlist中每个分类标签出现的频率，
    最后利用operator操作键值排序字典，
    并且返回出现次数最多的分类名称
    :param classlist:
    :return:
    """
    class_count = {};
    for vot in classlist:
        if vot not in class_count.keys():
            class_count[vot]=0;
        class_count[vot] +=1;
    sorted_class_count = sorted(class_count.iteritems(),
                                key=itemgetter(1),
                                reverse=True);
    print sorted_class_count;
    return sorted_class_count[0][0];



def create_tree(dataset, label):
    """
    创建树的函数代码
    :param dataset:
    :param label:标签列表包含了数据集中所有特征的标签，算法本身并不需要这个变量，但是为了给出数据明确的含义，我们将它作为一个输入参数提供。
    :return:
    """
    class_list = [example[-1] for example in dataset];


    # 类别完全相同则停止继续划分
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0];

    # 遍历完所有特征时返回出现次数最多的类别
    if len(dataset[0])==1:
        return majority_cnt([0]);

    # 找到当前最优特征指标index
    best_feat = choisir_meilleur_attribut_a_decouper(dataset);

    # 找到当前最优特征指标index对应的label
    best_feat_labal = label[best_feat];

    my_tree = {best_feat_labal:{}};
    del (label[best_feat]);

    # 得到列表包含的所有属性值
    feat_value = [example[best_feat] for example in dataset];
    feat_value_uniq = set(feat_value);
    for value in feat_value_uniq:
        sub_labels = label[:];
        my_tree[best_feat_labal][value] = create_tree(
            splitDataset(dataset, best_feat, value), sub_labels
        );
    return my_tree;