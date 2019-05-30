# -*- coding: utf-8 -*-
"""
Created on Sat May  30 12:59:24 2019

@author: Abhinits2046
"""

list = [4,53,2,6,57,3,543,4,53,63,75,74,233,5]

maxValue = list[0]# initialize list first index
minValue = list[0]
for i in range(0,len(list),1):
    if maxValue < list[i]:  # compare previous index value to next index value
        maxValue = list[i]
    if minValue > list[i]:
        minValue = list[i]

print("Minimum in list: ",minValue)
print("Maximum in list: ",maxValue)
