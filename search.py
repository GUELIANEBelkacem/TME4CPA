# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 22:20:07 2021

@author: moham
"""
import matplotlib.pyplot as plt
f1 = open("cc.txt", "r")
f2 = open("dd.txt", "r")
c = []
d = []
r = []
lines = f1.readlines()
for line in lines:                   
    c.append(int(line))
f1.close()
lines = f2.readlines()
for line in lines:                   
    d.append(int(line))
f2.close()

for i in range(len(c)):
    if(c[i] == 12 and d[i]>65):
        r.append(i)
# plt.figure()
# plt.scatter(d, c)
# #plt.title("Coreness by Degree")
# plt.xlabel("Degree")
# plt.ylabel("Coreness")


print(r)