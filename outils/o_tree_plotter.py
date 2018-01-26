# -*- coding: utf-8 -*-
#!/usr/bin/python

"""
用来绘制决策树
绘图区由create_plot.ax1 定义
"""

from matplotlib import pyplot;

# 定义文本框和箭头
dicision_node = dict(boxstyle="sawtooth", fc="0.8");
leaf_node = dict(boxstye="round64", fc="0.8");
arrow_args = dict(arrow_style="<-");

def create_plot():

    figure = pyplot(1, facecolor = "white");
    figure.clf();
    create_plot.ax1=pyplot.subplot(111, framon=False);
    plot_node('决策节点', (0.5, 0.1), (0.1, 0.5), dicision_node);
    plot_node('叶节点', (0.8, 0.1), (0.3, 0.8), leaf_node);
    figure.plot();


def plot_node(node_txt, center_pt, parent_pt, node_type):
    """
    使用文本注解绘制树节点
    :param node_txt:
    :param center_pt:
    :param parent_pt:
    :param node_type:
    :return:
    """
    create_plot.ax1.annotate(node_txt,
                             xy=parent_pt,
                             xycoords='axes fraction',
                             xytext=center_pt,
                             textcoords='axes fraction',
                             va='center',
                             ha='center',
                             bbox=node_type,
                             arrowprops=arrow_args)