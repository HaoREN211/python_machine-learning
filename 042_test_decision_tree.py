# -*- coding: utf-8 -*-
#!/usr/bin/python

from outils.o_trees import creer_dataset, create_tree;
dataset, label = creer_dataset();
print label;
print dataset;
my_tree = create_tree(dataset, label);
print my_tree;