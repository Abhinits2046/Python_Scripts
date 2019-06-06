# -*- coding: utf-8 -*-
"""
Created on Thu June  06 18:40:24 2019

@author: Abhinits2046
"""
f = 0
s = 1
num = int(input("Enter the number\t"))
while num>0:
    t= f+s
    f = s
    s = t
    num -= 1
    if num == 0:
        print(f)
