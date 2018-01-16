# -*- coding: utf-8 -*-
#!/usr/bin/python

from numpy import array;

dataset = [[1,2,3], [4,5,6],[7,8,9],[1,2,3]];
for i in range(3):
    liste_attribut = [exemple[i] for exemple in dataset];

    print i;
    print set(liste_attribut);
    print liste_attribut;