
from numpy import *;
import operator;
import  KNN;
k=2;
group, labels = KNN.createDataSet();
inX = array([0.2, 0.1]);
data_set_size = group.shape[0];



diffmat = tile(inX, (data_set_size, 1)) -group;
sqdiffmat = diffmat**2;
print sqdiffmat;
print ("---------------------");

sqdistances = sqdiffmat.sum(axis=1);
print sqdistances;
print ("---------------------");
distances = sqdistances**0.5;
sortdistanceindicies = distances.argsort();
print sortdistanceindicies;
print ("---------------------");
classc_count = {};
for i in range(k):
    vote_labels = labels[sortdistanceindicies[i]];
    classc_count[vote_labels]=classc_count.get(vote_labels, 0)+1;
print ("vote_labels---------------------");
print vote_labels;
print ("vote_labels---------------------");
print ("classc_count---------------------");
print classc_count;
print ("classc_count---------------------");
sorted_class_count = sorted(classc_count.iteritems(),
                            key=operator.itemgetter(1),
                            reverse=True);
print ("classc_count---------------------");
print(sorted_class_count[0][0]);
print ("classc_count---------------------");

print ("classc_count_all---------------------");
print(sorted_class_count);
print ("classc_count_all---------------------");