# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 20:00:24 2019

@author: Abhinits2046
"""
list = []
n = int(input("Enter the length of list\t"))
for i in range(n):
    listInput = int(input("Enter the elements and hit Enter\t"))
    list.append(listInput)

print("List = ",list)

even = 0
odd = 0
for i in list:
    if i%2 == 0:
        even += 1
    else:
        odd += 1

print("Total even numbers in list: ",even)
print("Total odd numbers in list: ", odd)