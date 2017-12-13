# -*- coding:utf-8 -*-

def prime(n):
    for x in range(2,n):
        is_prime = True    
        for y in range(2,x-1):
            if x%y==0:
                is_prime = False
                break
        if is_prime:
		print x,',',

prime(100)
