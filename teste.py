# -*- coding: utf-8 -*-
#!/usr/bin/python

import o_transfer_file_to_matrix;

teste = [1, 2, 3, 4];
print teste[0:3];

file_name = "./outils/021_txt_donnees";
group, labels = o_transfer_file_to_matrix.file_2_matrix(file_name, 3);

print "group", group;
print "labels", labels;