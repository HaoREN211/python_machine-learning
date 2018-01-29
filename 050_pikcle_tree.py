# -*- coding: utf-8 -*-
#!/usr/bin/python


from outils.o_trees import classyfy, creer_dataset, retrieve_tree, store_tree, grab_tree;
my_dataset, libelles = creer_dataset();
my_tree = retrieve_tree(0);

print ("my dataset is :");
print my_dataset;
print "my tree is : ";
print my_tree;

print classyfy(my_tree, libelles, [1, 0]);
print classyfy(my_tree, libelles, [1, 1]);


file_name = "classifier_storage.txt";
store_tree(my_tree, file_name);

seconde_tree = grab_tree(file_name);
print "seconde tree";
print seconde_tree;
