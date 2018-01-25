# -*- coding: utf-8 -*-
#!/usr/bin/python

from outils.o_trees import creer_dataset, choisir_meilleur_attribut_a_decouper, majority_cnt;

dataset, libelles = creer_dataset();
print "my dataset is :";
print dataset;
print "my libelles are:";
print libelles;
attribut = choisir_meilleur_attribut_a_decouper(dataset);
print "best feature is :"
print attribut;

"""
测试 majority_cnt
"""
class_list = [1,1,2,3,1,1,2];
resultat_sorted_class_list = majority_cnt(class_list);
print(resultat_sorted_class_list);