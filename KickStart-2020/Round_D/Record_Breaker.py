#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 02:40:58 2020

@author: AkashTyagi
"""

tc = int(input())
output = []

def c(arr,N):
    maxx = 0
    count = 0
    for i in range(N):
        prev =  i==0 or arr[i]>maxx
        nexxt = i==N-1 or arr[i]>arr[i+1]
        
        if prev and nexxt:
            count+=1
        maxx =max(arr[i],maxx)
    
    return count


for _ in range(tc):
    first_line = int(input())
    second_line = input()
    
    # a,b= [int(i) for i in first_line.split(" ")]
    arr = [int(i) for i in second_line.split()]
    output.append(c(arr,first_line))
    
for i,o in enumerate(output):
    print("Case #{}: {}".format(i+1, o))