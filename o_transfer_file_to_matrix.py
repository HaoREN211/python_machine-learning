# -*- coding: utf-8 -*-
#!/usr/bin/python
from numpy import *;
import re;

def file_2_matrix(file_name, nb_colonne):
    """
     将txt或者其他文档装换为N*nb_colonne矩阵    .
    """

    # 读取文件
    fichier = open(file_name);
    tous_les_lignes = fichier.readlines();
    nombre_ligne = len(tous_les_lignes);

    # 初始化一个nombre_ligne×nb_colonne的零矩阵
    resultat_matrix = zeros((nombre_ligne, nb_colonne));
    labels_vecteur = [];
    index = 0;

    """
     逐行读取数据
     以tab为分隔符将每行数据进行分割
     正则匹配分割后得到的浮点数据
     如果无匹陪结果 舍弃掉该行
    """
    for ligne in tous_les_lignes:
        contain_string_value = 1;
        ligne=ligne.strip();
        champs_de_lists = ligne.split("\t");
        current_colonne_index = 0;
        for current_colonne in champs_de_lists:
            matchObj = re.search(r'([0-9]+\.)?([0-9]+)', current_colonne);
            if matchObj:
                champs_de_lists[current_colonne_index] = float(matchObj.group());
            else:
                contain_string_value=0;
                break;
        if(contain_string_value==0):
            continue;
        resultat_matrix[index, :] = champs_de_lists[0:nb_colonne];
        labels_vecteur.append(int(champs_de_lists[-1]));
        index = index + 1;
    return  resultat_matrix[0:index, 0:nb_colonne], labels_vecteur;
