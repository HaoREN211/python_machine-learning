# -*- coding: utf-8 -*-
#!/usr/bin/python

from outils.o_trees import calcShannonEnt;
from outils.o_trees import creer_dataset;

my_dataset, my_libelle = creer_dataset();
resultat = calcShannonEnt(my_dataset);
print "resultat 1 : %f" % float(resultat);

my_dataset[0][-1] = 'hehehe';
resultat = calcShannonEnt(my_dataset);
print "resultat 2 : %f" % float(resultat);