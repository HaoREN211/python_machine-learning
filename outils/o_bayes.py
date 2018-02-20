# -*- coding: utf-8 -*-
#!/usr/bin/python

# from numpy import zeros
from numpy import ones, log

def load_data_set():
    """
    创建数据集
    :return:
    """
    posting_list = [
        ['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
        ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
        ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
        ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
        ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
        ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']
    ];


    """
    1代表侮辱性文字
    0代表正常言论
    """
    class_vecctor = [0,1,0,1,0,1];
    return posting_list, class_vecctor;



def create_vocab_list(data_set):
    """
    创建单词列表
    :param data_set:
    :return:
    """

    # 创建一个空集
    vocab_set = set([]);

    for document in data_set:
        """
        创建两个集合的并集
        """
        vocab_set = vocab_set | set(document);
    return list(vocab_set);



def set_of_words_2_vec(vocab_list, input_set):
    """
    统计vocab_list里的单词在input_set里出现的次数
    :param vocab_list:
    :param input_set:
    :return:
    """
    return_vec = [0] * len(vocab_list)
    for word in input_set:
        if (word in vocab_list):
            return_vec[vocab_list.index(word)] =1
        else:
            print "the word : %s is not in my vocabulary!" % word
    return return_vec



def train_nb_0(train_matrix, train_category):
    """
    朴素贝叶斯分类器训练函数
    :param train_matrix: 训练集
    :param train_category: 训练集分类
    :return:
    """

    num_train_docs = len(train_matrix)
    num_words = len(train_matrix[0])

    # 初始化概率
    p_abusive =  sum(train_category) /float(num_train_docs)
    # p0_num = zeros(num_words)
    # p1_num = zeros(num_words)
    p0_num = ones(num_words)
    p1_num = ones(num_words)
    # p0_denom = 0.0
    # p1_denom = float(0.0)
    p0_denom = 2.0
    p1_denom = float(2.0)

    for i in range(num_train_docs):
        """
        p_num 每个词在每个类别中出现的次数
        p_denom 每个类别中所有词出现的总次数
        """
        if(train_category[i] ==1):
            p1_num += train_matrix[i]
            p1_denom += sum(train_matrix[i])
        else:
            p0_num += train_matrix[i]
            p0_denom += sum(train_matrix[i])

    p1_vect = log(p1_num/p1_denom)
    p0_vect = log(p0_num/p0_denom)
    return p0_vect, p1_vect, p_abusive;