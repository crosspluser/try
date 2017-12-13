# -*- coding:utf-8 -*-
def fib(n=1000): #Fibonacci
    """Print Fibonacci"""
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a+b

#call func

fib(2000)
