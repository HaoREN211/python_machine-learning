#!/usr/bin/python

from numpy import *;
import  operator;

def createDataSet() :
    groupe = array([[1.0, 1.1],[1.0, 1.0],[0, 0],[0, 0.1]]);
    labels = ['A', 'A', 'B', 'B'];
    return groupe, labels;

def classify0(inX, dataset, labels, k):
    #nombre de enregistrement
    datasetsize = dataset.shape[0];

    #difference de chaque attribut
    diffmat = tile(inX, (datasetsize, 1)) -dataset;

    #carre de chaque attribut.
    sqdiffmat = diffmat**2;

    #calcul par chaque ligne
    sqdistances = sqdiffmat.sum(axis=1);

    #calcul de distance entre le point a tester avec les points d'apprentissage
    distances = sqdistances**0.5;

    #recuperer la liste de indice d'ordre de distance en ordre croissant de chaque point apprentissage
    sortdistanceindicies = distances.argsort();
    classc_count = {};

    #calculer le nombre de libelle de k premier point
    for i in range(k):
        vote_labels = labels[sortdistanceindicies[i]];
        classc_count[vote_labels]=classc_count.get(vote_labels, 0)+1;
    sorted_class_count = sorted(classc_count.iteritems(),
                                key=operator.itemgetter(1),
                                reverse=True);
    return sorted_class_count[0][0];