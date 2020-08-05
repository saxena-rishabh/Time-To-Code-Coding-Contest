# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 14:33:50 2020

@author: Rishabh
"""
import math

t = int(input())

for z in range(t):
    count = 0
    n = int(input())
    s = input()
    for i in s:
        if i in ['A', 'E', 'I', 'O', 'U']:
            count+=1
    
    if count!=0:
        print( math.factorial(n-count+1) * math.factorial(count))
    else:
        print(math.factorial(n))