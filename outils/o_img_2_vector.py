# -*- coding: utf-8 -*-
#!/usr/bin/python

from numpy import zeros;

def img_2_vector(file_name):
    """
    Convertir l'image vers un vecteur.
    :param file_name: le chemin de l'image
    :return: a vecteur de diension 1024
    """

    resultat = zeros((1, 1024));
    fichier = open(file_name);
    for i in range(32):
        ligne_fichier = fichier.readline();
        for j in range(32):
            resultat[0, i*32+j] = (ligne_fichier[j]);