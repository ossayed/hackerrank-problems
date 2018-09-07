#!/bin/python3

import sys


https://www.hackerrank.com/challenges/mini-max-sum/problem


sum_max = 0
sum_real = 0
sum_list = []
arr = list(map(int, input().strip().split(' ')))
for x in  range(0,len(arr)):
    sum_max = sum_max + arr[x]

for x in range(0,len(arr)):
    sum_real = sum_max - arr[x]
    sum_list.append(sum_real)
print(min(sum_list), max(sum_list))
    
