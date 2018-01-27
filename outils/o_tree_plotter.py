# -*- coding: utf-8 -*-
#!/usr/bin/python

"""
用来绘制决策树
绘图区由create_plot.ax1 定义

create_plot 是我们使用的主函数
绘制树形图的很多工作都是在函数plot_tree()中完成的

全局变量 plot_tree.totalW存储树的宽度
全局变量 plot_tree.totalD存储树的深度
我们使用这两个变量计算树节点的摆放位置
这样可以将树绘制在水平方向和垂直方向的中心位置。

树的宽度用于计算放置判断节点的位置
主要的计算原则是将它放在所有叶子节点的中间

使用两个全局变量
plot_tree.xOff, plot_tree.yOff 追踪已经绘制的节点位置
以及放置下一个节点的恰当位置

通过计算树包含的所有叶子节点数，
划分图形的宽度
从而计算得到当前节点的中心位置
我们按照叶子节点的数目将x轴划分尾若干部分
按照图形比例绘制树形图。
"""

from matplotlib import pyplot;
pyplot.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
pyplot.rcParams['axes.unicode_minus']=False #用来正常显示负号

# 定义文本框和箭头
dicision_node = dict(boxstyle="sawtooth", fc="0.8");
leaf_node = dict(boxstye="round64", fc="0.8");
arrow_args = dict(arrowstyle="<-");


def create_plot_sauvegarde():
    """
    :return:
    """
    fig = pyplot.figure(1, facecolor='white');
    fig.clf();
    create_plot.ax1 = pyplot.subplot(111, frameon=False);
    plot_node('Decision Node', (0.5, 0.1), (0.1, 0.5), dicision_node);
    plot_node('Leaf Node', (0.8, 0.1), (0.3, 0.8), leaf_node);
    pyplot.show();


def create_plot(in_tree):
    """
    :return:
    """
    fig = pyplot.figure(1, facecolor='white');
    fig.clf();
    axprops = dict(xticks=[], yticks=[]);
    create_plot.ax1 = pyplot.subplot(111, frameon=False, **axprops);
    plot_tree.totalW = float(get_num_leafs(in_tree));
    plot_tree.totalD = float(get_depth_of_tree(in_tree));
    plot_tree.xOff = -0.5/ plot_tree.totalW ;
    plot_tree.yOff = 1.0;
    plot_tree(in_tree, (0.5, 1.0), '');
    pyplot.show();


def plot_node(node_txt, center_pt, parent_pt, node_type):
    """
    使用文本注解绘制树节点
    :param node_txt:
    :param center_pt:
    :param parent_pt:
    :param node_type:
    :return:
    """
    #create_plot.ax1.annotate(node_txt, xy=parent_pt, xycoords='axes fraction', xytext=center_pt,
    #                         textcoords='axes fraction', va='center', ha='center', bbox=node_type,
    #                         arrowprops=arrow_args);
    create_plot.ax1.annotate(node_txt,
                             xy=parent_pt,
                             xycoords="axes fraction",
                             xytext=center_pt,
                             textcoords="axes fraction",
                             va="center",
                             ha="center",
                             bbox=dict(boxstyle="round", fc="w"),
                             arrowprops=arrow_args);


def define_tree():
    """
    返回上节得到的树
    :return:
    """
    return {'no surfacing': {
                0: 'no',
                1: {
                         'flippers': {
                             0: 'no',
                             1: 'yes'}}}};

def retrieve_tree(i):
    """
    返回上节得到的树和一颗新的树
    :param i:
    :return:
    """
    list_of_tree = [
        {'no surfacing': {
            0: 'no',
            1: {
                'flippers': {
                    0: 'no',
                    1: 'yes'}}}},
        {'no surfacing': {
            0: 'no',
            1: {
                'flippers': {
                    0: {
                      'head':{
                          0:'no',
                          1:'yes'
                      }
                    },
                    1: 'yes'}}}}
    ]
    return list_of_tree[i];


def get_num_leafs(my_tree):
    """
    取回树的叶节点数目
    :param my_tree:
    :return:
    """
    number_leaf = 0;
    first_str = my_tree.keys()[0];
    seconde_dict = my_tree[first_str];
    for key in seconde_dict.keys():
        """
        type 函数用来判断类型
        这里用递归判断叶节点数目
        """
        if type(seconde_dict[key]).__name__=='dict':
            number_leaf += get_num_leafs(seconde_dict[key]);
        else:
            number_leaf +=1;
    return number_leaf;

def get_depth_of_tree(my_tree):
    """
    计算树的层数
    :param my_tree:
    :return:
    """
    max_depth = 0;
    root_node = my_tree.keys()[0];
    seconde_tree = my_tree[root_node];
    for cle in seconde_tree.keys():
        if type(seconde_tree[cle]).__name__ == 'dict':
            this_depth = 1 + get_depth_of_tree(seconde_tree[cle]);
        else:
            this_depth = 1;
        if this_depth > max_depth:
            max_depth = this_depth;
    return max_depth;



def plot_mid_text(cntr_pt,
                  parent_pt,
                  txt_string):
    """
    在父子节点间填充文本信息
    :param cntr_pt: 子节点
    :param parent_pt: 父节点
    :param txt_string: 要加的文本信息
    :return:
    """
    x_mid = (parent_pt[0] - cntr_pt[0])/float(2.0) + cntr_pt[0];
    y_mid = (parent_pt[1] - cntr_pt[1]) / float(2.0) + cntr_pt[1];
    create_plot.ax1.text(x_mid, y_mid, txt_string);


def plot_tree(my_tree,
              parent_pt,
              node_text):
    """
    :param my_tree:
    :param parent_pt:
    :param node_text:
    :return:
    """
    # 计算树的叶节点数目
    # 树的宽度用于计算放置判断节点的位置
    # 主要的计算原则是将它放在所有叶子节点的中间
    number_leaf = get_num_leafs(my_tree);

    # 计算树的高度
    number_depth = get_depth_of_tree(my_tree);

    root_node = my_tree.keys()[0];
    cntr_pt = (plot_tree.xOff+(float(1.0) + float(number_leaf))/float(2.0)/plot_tree.totalW,
               plot_tree.yOff);
    plot_mid_text(cntr_pt, parent_pt, node_text);
    plot_node(root_node,
              cntr_pt,
              parent_pt,
              dicision_node);
    sub_tree = my_tree[root_node];
    plot_tree.yOff = plot_tree.yOff - 1.0/plot_tree.totalD;
    """
    第一次迭代只画出root节点
    第二次画出第二层节点 以及和root的连线
    """
    for cle in sub_tree.keys():
        if type(sub_tree[cle]).__name__ == 'dict':
            plot_tree(sub_tree[cle], cntr_pt, str(cle));
        else:
            plot_tree.xOff = plot_tree.xOff + 1.0/plot_tree.totalW;
            plot_node(sub_tree[cle],
                      (plot_tree.xOff ,plot_tree.yOff ),
                      cntr_pt,
                      leaf_node);
            plot_mid_text(
                (plot_tree.xOff, plot_tree.yOff),
                cntr_pt,
                str(cle)
            );
    plot_tree.yOff = plot_tree.yOff + 1.0/plot_tree.totalD;