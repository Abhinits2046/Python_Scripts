# -*- coding: utf-8 -*-
"""
Created on Sat May  25 11:15:45 2019

@author: Abhinits2046
"""

#program to transpose a matrix
#using nested loop
X = [[12,7],
     [4,5],
     [3,8]]
result = [[0,0,0],
          [0,0,0]]


#iterate through rows
for i in range(len(X)):
    #iterate through columns
    for j in range(len(X[0])):
        result[j][i] = X[i][j]
    for r in result:
        print(r)
        
        
