# -*- coding: utf-8 -*-
# !/usr/bin/python

import random
from numpy import matrix as mat
from numpy import shape
from numpy import zeros
from numpy import multiply


def load_data_set(file_name):
    """
    读入文件的内容，第一二列分别为第一二个特征
    第三列为标签
    :param file_name:文本路径
    :return:
    """
    data_mat = []
    label_mat = []
    fr = open(file_name)
    for line in fr.readlines():
        line_arr = line.strip().split('\t')
        data_mat.append([float(line_arr[0]), float(line_arr[1])])
        label_mat.append(float(line_arr[2]))
    return data_mat, label_mat


def select_j_rand(i, m):
    """
    返回不等于i并且小于等于m的数
    :param i: 当前alpha的下标
    :param m: alpha的总数目
    :return:
    """
    j = i
    while j == i:
        j = int(random.uniform(0, m))
    return j


def clip_alpha(aj, h, l):
    """
    用于调整大于h和小于l的aj值
    :param aj:
    :param h:
    :param l:
    :return:
    """
    if aj > h:
        aj = h
    if l > aj:
        aj = l
    return aj


def smo_simple(data_mat_in, class_labels, c, toler, max_iter):
    data_matrix = mat(data_mat_in)
    label_matrix = mat(class_labels).transpose()
    b = 0
    m, n = shape(data_matrix)
    alpha = mat(zeros((m, 1)))
    itertation = 0
    while itertation < max_iter:
        alpha_pairs_changed = 0
        for i in range(m):
            # 预测的类别
            f_xi = float(multiply(alpha, label_matrix).T *
                         (data_matrix * data_matrix[i, :].T)) + b

            # 误差
            e_i = f_xi - float(label_matrix[i])

            if ((label_matrix[i]*e_i < -toler) and (alpha[i] < c)) \
                    or ((label_matrix[i]*e_i > toler) and (alpha[i] > 0)):
                j = select_j_rand(i, m)
                f_xj = float(multiply(alpha, label_matrix).T *
                             (data_matrix * data_matrix[j, :].T)) + b
                e_j = f_xj - float(label_matrix[j])
                alpha_i_old = alpha[i].copy()
                alpha_j_old = alpha[j].copy()

                if label_matrix[i] != label_matrix[j]:
                    l = max(0, alpha[j] - alpha[i])
                    h = min(c, c + alpha[j] - alpha[i])
                else:
                    l = max(0, alpha[j] + alpha[i] - c)
                    h = min(c, alpha[j] + alpha[i])

                if l == h:
                    print("l == h")
                    continue
                eta = 2.0 * data_matrix[i, :] * data_matrix[j, :].T - \
                      data_matrix[i, :] * data_matrix[i, :].T - \
                      data_matrix[j, :] * data_matrix[j, :].T
                if eta >= 0:
                    print("eta >= 0")
                    continue
                alpha[j] -= label_matrix[j] * (e_i - e_j) / eta
                alpha[j] = clip_alpha(alpha[j], h, l)
                if abs(alpha[j] - alpha_j_old) < 0.00001:
                    print("j not moving enough")
                    continue
                alpha[i] += label_matrix[j] * label_matrix[i] * \
                            (alpha_j_old - alpha_i_old)
                b1 = b - e_i - label_matrix[i] * (alpha[i] - alpha_i_old) * \
                     data_matrix[i, :] * data_matrix[i, :].T - \
                     label_matrix[j] * (alpha[j] - alpha_j_old) * \
                     data_matrix[i, :] * data_matrix[j, :].T
                b2 = b - e_j - label_matrix[i] * (alpha[i] - alpha_i_old) * \
                     data_matrix[i, :] * data_matrix[j, :].T - \
                     label_matrix[j] * (alpha[j] - alpha_j_old) * \
                     data_matrix[j, :] * data_matrix[j, :].T
                if (0 < alpha[i]) and (c > alpha[i]):
                    b = b1
                elif (0 < alpha[j]) and (c > alpha[j]):
                    b = b2
                else:
                    b = (b1 + b2)/2.0
                alpha_pairs_changed += 1
        if alpha_pairs_changed == 0:
            itertation += 1
        else:
            itertation = 0
    return b, alpha


def smoSimple(dataMatIn, classLabels, C, toler, maxIter):
    dataMatrix = mat(dataMatIn); labelMat = mat(classLabels).transpose()
    b = 0; m,n = shape(dataMatrix)
    alphas = mat(zeros((m,1)))
    iter = 0
    while (iter < maxIter):
        alphaPairsChanged = 0
        for i in range(m):
            fXi = float(multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[i,:].T)) + b
            Ei = fXi - float(labelMat[i])#if checks if an example violates KKT conditions
            if ((labelMat[i]*Ei < -toler) and (alphas[i] < C)) or ((labelMat[i]*Ei > toler) and (alphas[i] > 0)):
                j = select_j_rand(i,m)
                fXj = float(multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[j,:].T)) + b
                Ej = fXj - float(labelMat[j])
                alphaIold = alphas[i].copy(); alphaJold = alphas[j].copy();
                if (labelMat[i] != labelMat[j]):
                    L = max(0, alphas[j] - alphas[i])
                    H = min(C, C + alphas[j] - alphas[i])
                else:
                    L = max(0, alphas[j] + alphas[i] - C)
                    H = min(C, alphas[j] + alphas[i])
                if L==H:
                    print ("L==H")
                    continue
                eta = 2.0 * dataMatrix[i,:]*dataMatrix[j,:].T - dataMatrix[i,:]*dataMatrix[i,:].T - dataMatrix[j,:]*dataMatrix[j,:].T
                if eta >= 0:
                    print ("eta>=0")
                    continue
                alphas[j] -= labelMat[j]*(Ei - Ej)/eta
                alphas[j] = clip_alpha(alphas[j],H,L)
                if (abs(alphas[j] - alphaJold) < 0.00001):
                    print ("j not moving enough")
                    continue
                alphas[i] += labelMat[j]*labelMat[i]*(alphaJold - alphas[j])
                b1 = b - Ei- labelMat[i]*(alphas[i]-alphaIold)*dataMatrix[i,:]*dataMatrix[i,:].T - labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[i,:]*dataMatrix[j,:].T
                b2 = b - Ej- labelMat[i]*(alphas[i]-alphaIold)*dataMatrix[i,:]*dataMatrix[j,:].T - labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[j,:]*dataMatrix[j,:].T
                if (0 < alphas[i]) and (C > alphas[i]): b = b1
                elif (0 < alphas[j]) and (C > alphas[j]): b = b2
                else: b = (b1 + b2)/2.0
                alphaPairsChanged += 1
        if (alphaPairsChanged == 0): iter += 1
        else: iter = 0
    return b,alphas