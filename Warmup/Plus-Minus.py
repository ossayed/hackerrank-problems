#!/bin/python3

import sys


https://www.hackerrank.com/challenges/plus-minus/problem


pos_nums = 0
neg_nums = 0
zero_nums = 0

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

for x in range(0,n):
    if(arr[x] > 0):
        pos_nums += 1
        
    elif(arr[x] < 0):
        neg_nums += 1
        
    else:
        zero_nums += 1
        
print(pos_nums/n)
print(neg_nums/n)
print(zero_nums/n)
     