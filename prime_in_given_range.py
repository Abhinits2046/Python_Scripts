# -*- coding: utf-8 -*-
"""
Created on Thu June  18 18:40:24 2019

@author: Abhinits2046
"""
# we assume r is range
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)