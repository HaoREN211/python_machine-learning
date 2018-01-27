# -*- coding: utf-8 -*-
#!/usr/bin/python

from outils.o_trees import creer_dataset, create_tree;
dataset, label = creer_dataset();
print label;
print dataset;
my_tree = create_tree(dataset, label);
print my_tree;

root_node = my_tree.keys()[0];
print("root_node");
print(root_node);

print("seconde tree");
print(my_tree[root_node]);

secoden_tree = my_tree[root_node];
secoden_node = my_tree[root_node].keys();
print"secoden node";
print(secoden_node);


print" first secoden node type";
print(type(secoden_tree[secoden_node[0]]).__name__);

print" econde secoden node type";
print(type(secoden_tree[secoden_node[1]]).__name__);
print(type(secoden_tree[secoden_node[1]]));