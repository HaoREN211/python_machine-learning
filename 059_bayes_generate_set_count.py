# -*- coding: utf-8 -*-
#!/usr/bin/python

from outils.o_bayes import load_data_set, \
    create_vocab_list, \
    set_of_words_2_vec, \
    train_nb_0


"""
测试 
    导入文档数组 
    导出文档中出现所有单词的列表 
"""
list_of_posts, list_classes = load_data_set()
my_vocabulary = create_vocab_list(list_of_posts)
count_vacabulary = set_of_words_2_vec(my_vocabulary, list_of_posts[0])


"""
计算每个词在每个文档中是否出现
"""
train_mat = []
for postin_doc in list_of_posts:
    train_mat.append(set_of_words_2_vec(my_vocabulary, postin_doc))
po_v, p1_v, p_ab = train_nb_0(train_mat, list_classes)

print sum(po_v)
print sum(p1_v)