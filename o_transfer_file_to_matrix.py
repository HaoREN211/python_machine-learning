# -*- coding: utf-8 -*-
#!/usr/bin/python
from numpy import *;

def file_2_matrix(file_name, nb_colonne):
    """
    将txt或者其他文档装换为N*nb_colonne矩阵    .
    """

    fichier = open(file_name);
    tous_les_lignes = fichier.readlines();
    nombre_ligne = len(tous_les_lignes);
    resultat_matrix = zeros((nombre_ligne, nb_colonne));
    labels_vecteur = [];
    index = 0;
    for ligne in tous_les_lignes:
        ligne=ligne.strip();
        champs_de_lists = ligne.split("\t");
        resultat_matrix[index, 0:nb_colonne] = champs_de_lists[0:nb_colonne];
        labels_vecteur.append(int(champs_de_lists[-1]));
        index = index + 1;
    return  resultat_matrix, labels_vecteur;
