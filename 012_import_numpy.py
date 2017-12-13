#!/usr/bin/python

from numpy import *;

#generation d'une table de int
rand_array = random.rand(4,4);
print("array : ");
print(rand_array);

#convertir de la table vers matrice
rand_matrix = mat(rand_array);
print("matrix : ");
print(rand_matrix);

#Calculer la matrice inverse
rand_matrix_inverse = rand_matrix.I;
print("matrix inverse : ");
print (rand_matrix_inverse);

resultat = rand_matrix*rand_matrix_inverse;
print ("\n\nLe resultat : ");
print (resultat);
