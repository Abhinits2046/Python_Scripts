# -*- coding: utf-8 -*-
"""
Created on Sat May  25 12:59:24 2019

@author: Abhinits2046
"""

#   Factorial(n)
#      computes n!
#     returns the factorial of n
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
def main():
    # try out the factorial function
    print(" 0! = ", factorial(0))
    print(" 1! = ", factorial(1))
    print(" 2! = ", factorial(2))
    print(" 5! = ", factorial(5))
    print(" 10! = ", factorial(10))
    print(" 20! = ", factorial(20))
    
main()
