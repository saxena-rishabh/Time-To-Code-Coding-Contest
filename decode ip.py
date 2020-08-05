# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 14:16:21 2020

@author: Rishabh
"""

ip = input()
ip = ip.replace(".", "")
new_ip = sorted(ip)
final = []
for i in range(0, len(new_ip), 8):
    temp = new_ip[i]
    t1 = ord(temp)
    last = bin(t1-65)[2:]
    zeros = 7 - len(last)
    num = '1' + '0' * zeros + last
    final.append(num)

print('.'.join(final))
    
    
    
