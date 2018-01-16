# -*- coding: utf-8 -*-
#!/usr/bin/python

from outils.o_trees import creer_dataset, choisir_meilleur_attribut_a_decouper;

dataset, libelles = creer_dataset();
print "my dataset is :";
print dataset;
print "my libelles are:";
print libelles;
attribut = choisir_meilleur_attribut_a_decouper(dataset);
print "best feature is :"
print attribut;