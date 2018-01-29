# -*- coding: utf-8 -*-
#!/usr/bin/python

from outils.o_trees import create_tree;
from outils.o_tree_plotter import create_plot;

fr = open('./donnees/d_lenses.txt');
lenses = [ligne.strip().split('\t') for ligne in fr.readlines()];
print "My dataset is : ";
print lenses;

lenses_label = ['age', 'prescrip', 'astigmatic', 'tear_rate'];

lenses_tree = create_tree(lenses, lenses_label);
print "My tree is : ";
print lenses_tree;
create_plot(lenses_tree);
