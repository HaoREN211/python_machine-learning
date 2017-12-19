# -*- coding: utf-8 -*-
#!/usr/bin/python
# 一个简单介绍matplotlib的例子 .

from numpy import *;
"""
 matplotlib.pyplot需安装 python-tk
 sudo apt-get install python-tk
"""
import matplotlib.pyplot as plt;
import o_transfer_file_to_matrix;
import time;

# 导入txt文件并将其转换成矩阵
# file_name = "./outils/021_txt_donnees";
file_name = "./donnees/d_datingTestSet2.txt";
groupe, libelles = o_transfer_file_to_matrix.file_2_matrix(file_name, 3);

print  groupe.shape;

# 创建一幅图
tableau = plt.figure();



"""
 ax = fig.add_subplot(349)
 参数349的意思是：将画布分割成3行4列，图像画在从左到右从上到下的第9块
"""
ax = tableau.add_subplot(111);



"""
 scatter
 基本散列点绘制
"""
# ax.scatter(groupe[:,1], groupe[:,2]);
ax.scatter(groupe[:,1], groupe[:,2], 15.0*array(libelles), 15.0*array(libelles));



# 显示
tableau.show();
time.sleep(10);

# plt.ion() #开启interactive mode
# plt.figure(1) # 创建图表1
# plt.plot(groupe[:,1], groupe[:,2])
# plt.draw()
# time.sleep(5)
# plt.close(1)