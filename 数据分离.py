# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 11:21:57 2018

@author: X
"""

f=open('山西招生人数.txt',encoding='gbk').readlines()
ls=[]
data=[]
for line in f:
    ls.append(str(line.split('(')[1].split(',')[0]))
    data.append(int(line.split(',')[1].split(')')[0]))
    print(ls)
    print(data)