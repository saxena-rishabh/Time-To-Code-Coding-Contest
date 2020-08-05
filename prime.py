# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 15:16:11 2020

@author: Rishabh
"""

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

t = int(input())

for z in range(t):
    n = int(input())
    numbers = list(map(int,input().split())) 
    final = []
    for i in numbers:
        final.append(sum(prime_factors(i)))
    final.sort(reverse=True)
    print(*final)




 

