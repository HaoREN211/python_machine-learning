# -*- coding: utf-8 -*-
#!/usr/bin/python

# from numpy import zeros
from numpy import ones, log, array

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
    统计vocab_list里的单词在input_set里是否出现
    词集模式
    :param vocab_list:
    :param input_set:
    :return:
    """
    return_vec = [0] * len(vocab_list)
    for word in input_set:
        if (word in vocab_list):
            return_vec[vocab_list.index(word)] =1
        else:
            print ("the word : %s is not in my vocabulary!" % word)
    return return_vec



def bag_of_words_2_vec(vocab_list, input_set):
    """
    统计vocab_list里的单词在input_set里出现的次数
    词袋模式
    :param vocab_list:
    :param input_set:
    :return:
    """
    return_vec = [0] * len(vocab_list)
    for word in input_set:
        if (word in vocab_list):
            return_vec[vocab_list.index(word)] += 1
        else:
            print ("the word : %s is not in my vocabulary!" % word)
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



def classify_nb(vect_to_classify, p0_vect, p1_vect, p_class_1):
    """
    分类器
    :param vect_to_classify:
    :param p0_vect:    P(w | c2)
    :param p1_vect:    P(w | c1)
    :param p_class_1:  P(c1)
    :return:
    """

    # log 让相乘变为相加，sum和后面的加是一个原理
    p1 = sum(vect_to_classify*p1_vect) + log(p_class_1)
    p0 = sum(vect_to_classify * p0_vect) + log(1 - p_class_1)
    if(p1 > p0):
        return 1
    else:
        return 0


def test_nb():
    """
    测试分类器
    :return:
    """

    list_of_post, list_of_category = load_data_set()
    my_vocabulary = create_vocab_list(list_of_post)
    train_mat = []
    for post in list_of_post:
        train_mat.append(set_of_words_2_vec(my_vocabulary, post))
    p0_v, p1_v, p_ab = train_nb_0(train_mat, list_of_category)

    test_entry = ['love', 'my', 'dalmation']
    this_doc = array(set_of_words_2_vec(my_vocabulary, test_entry))
    resultat1 = classify_nb(this_doc, p0_v, p1_v, p_ab)
    print ("result is %s " % resultat1)

    test_entry = ['stupid', 'garbage']
    this_doc = array(set_of_words_2_vec(my_vocabulary, test_entry))
    resultat = classify_nb(this_doc, p0_v, p1_v, p_ab)
    print ("result is %s " % resultat)
    return resultat1, resultat



def text_parse(big_string):
    """
    将字符串转换为单词列表
    :param big_string:
    :return:
    """
    import re
    list_of_token = re.split('\\W*', big_string)
    return [token.lower() for token in list_of_token if len(token)>0]