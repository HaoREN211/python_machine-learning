# -*- coding: utf-8 -*-
#!/usr/bin/python

from outils.o_tree_plotter import define_tree, get_num_leafs, retrieve_tree, get_depth_of_tree;

my_tree = define_tree();
my_tree = retrieve_tree(1);
num_leag = get_num_leafs(my_tree);
num_deptp = get_depth_of_tree(my_tree);

print "My tree is : ";
print my_tree;
print "Number of leaf is : ";
print num_leag;
print "Number of depth : ";
print num_deptp;