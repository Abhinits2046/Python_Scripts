# -*- coding: utf-8 -*-
"""
Created on Thu June  06 18:40:24 2019

@author: Abhinits2046
"""
num = int(input("Enter the number"))
reverse =0
while num>0:
    remender = num%10
    reverse  = (reverse*10)+remender
    num = num//10
    if num == 0:
        print(reverse)
