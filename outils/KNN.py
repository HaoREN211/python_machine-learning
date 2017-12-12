#!/usr/bin/python

from numpy import *;
import  operator;

def createDataSet() :
    groupe = array([[1.0, 1.1],[1.0, 1.0],[0, 0],[0, 0.1]]);
    labels = ['A', 'A', 'B', 'B'];
    return groupe, labels;

def classify0(inX, dataset, labels, k):
    datasetsize = dataset.shape[0];
    diffmat = tile(inX, (datasetsize, 1)) -dataset;
    sqdiffmat = diffmat**2;
    sqdistances = sqdiffmat.sum(axis=1);
    distances = sqdistances**0.5;
    sortdistanceindicies = distances.argsort();
    classc_count = {};
    for i in range(k):
        vote_labels = labels[sortdistanceindicies[i]];
        classc_count[vote_labels]=classc_count.get(vote_labels, 0)+1;
    sorted_class_count = sorted(classc_count.iteritems(),
                                key=operator.itemgetter(1),
                                reverse=True);
    return sorted_class_count[0][0];