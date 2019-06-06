# -*- coding: utf-8 -*-
"""
Created on Thu June  06 18:40:24 2019

@author: Abhinits2046
"""
num = int(input("Enter number to check prime \t"))
c= 2
while (c*c) <= num:
    if num%c == 0:
        print("\nNumber is not Prime because devisible by",c)
        a = 1
        exit()
    c += 1
print("Prime")



