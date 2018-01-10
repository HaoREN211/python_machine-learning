# -*- coding: utf-8 -*-
#!/usr/bin/python

from outils.o_trees import splitDataset, creer_dataset;

dataset, libelles = creer_dataset();
print "dataset:"
print dataset;

resultat = splitDataset(dataset, 0, 0);
print "axis 0 = 0";
print resultat;

resultat = splitDataset(dataset, 0, 1);
print "axis 0 = 1";
print resultat;