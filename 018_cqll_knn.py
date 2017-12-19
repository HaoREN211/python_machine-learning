# -*- coding: utf-8 -*-

import outils.o_KNN as methode_KNN;

groupe, labels = methode_KNN.createDataSet();

print (groupe, labels);


# 用训练集数据groupe和他们所在类别labels来测试KNN近邻算法的结果
point = [0.9, 0.7];
resultat = methode_KNN.classify0(point, groupe, labels, k=2);
print point, " est appartenu par le groupe " ,resultat, ";"

