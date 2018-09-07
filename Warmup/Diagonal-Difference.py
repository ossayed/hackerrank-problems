#!/bin/python3

import sys


#https://www.hackerrank.com/challenges/diagonal-difference/problem


dia0_sum = 0
dia1_sum = 0
n = int(input().strip())
a = []
dia0 = []
dia1 = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
    
for x in range(0,n):
    dia0.append(a[x][x])
    y = x + 1
    dia1.append(a[x][n-y])


for x in range(0,n):
    dia0_sum = dia0_sum + dia0[x]
    dia1_sum = dia1_sum + dia1[x]
print(abs(dia0_sum - dia1_sum))
    
    
    
