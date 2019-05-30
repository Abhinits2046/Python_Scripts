# -*- coding: utf-8 -*-
"""
Created on Sat May  30 12:59:24 2019

@author: Abhinits2046
"""

s = input("Enter the buffer data\n")
l = len(s)

i = 0
while i<l:    # outer loop
    num = ''
    symbol = s[i]
    while symbol.isdigit(): # inner loop
        num += symbol
        i += 1
        if i <l:      # loop to take number from garbage contains more than one digit
            symbol = s[i]
        else:
            break
    if num != '':
        print(num)
    i += 1

# Enter the buffer data
# abhishek age 20 doby 1998
#
# 20
# 1998