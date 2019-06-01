# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 20:00:24 2019

@author: Abhinits2046
"""
list = []
n = int(input("Enter the length of list\t"))
for i in range(n):
    userInput = int(input("Enter the element and Hit Enter\t"))
    list.append(userInput)

print(list)

negative = []
positive = []
for i in list:
    if i < 0:
        negative.append(i)
    if i>0:
        positive.append(i)

print("Negative Elements: ",negative)
print("Positive Elements: ",positive)