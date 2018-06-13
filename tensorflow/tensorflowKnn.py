#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

import tensorflow as tf
import tensorflow.examples.tutorials.mnist.input_data as input_data


old_v = tf.logging.get_verbosity()
tf.logging.set_verbosity(tf.logging.ERROR)

# 最近邻算法，此代码实现类似1-NN
# 导入输入数据MNIST

mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)
#这个例子限制了样本的数目
Xtr, Ytr = mnist.train.next_batch(1000)
# 1000 条候选样本，测试样本跟候选样本比较，得到最近的K个样本，然后k个样本的标签大多数为某类，测试样本就为某类

Xte, Yte = mnist.test.next_batch(200)
# 200 条测试样本

# tf Graph Input，占位符，用来feed数据
xtr = tf.placeholder("float", [None, 784])
xte = tf.placeholder("float", [784])

# 最近邻计算距离使用 L1 距离
# 计算L1距离
distance = tf.reduce_sum(tf.abs(tf.add(xtr, tf.negative(xte))), reduction_indices=1)
# 预测: 获取离测试样本具有最小L1距离的样本(1-NN），此样本的类别作为test样本的类别
pred = tf.arg_min(distance, 0)

accuracy = 0.


# 初始化图
init = tf.global_variables_initializer()

# 发布图
with tf.Session() as sess:
    sess.run(init)

    #循环测试集
    for i in range(len(Xte)):
        # Get nearest neighbor
        nn_index = sess.run(pred, feed_dict={xtr: Xtr, xte: Xte[i, :]})  #每次循环feed数据，候选Xtr全部，测试集Xte一次循环输入一条
        # 获得与测试样本最近样本的类别，计算与真实类别的误差
        print("Test", i, "Prediction:", np.argmax(Ytr[nn_index]), \
              "True Class:", np.argmax(Yte[i]))
        # 计算误差率
        if np.argmax(Ytr[nn_index]) == np.argmax(Yte[i]):
            accuracy += 1. / len(Xte)
    print("Done!")
    print("Accuracy:", accuracy)