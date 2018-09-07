#!/bin/python3

import sys


#https://www.hackerrank.com/challenges/a-very-big-sum/problem


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

def sum_num():
    sum = 0
    for i in range(n):
        sum = sum + arr[i]
        
    print(sum)
    
sum_num()
        