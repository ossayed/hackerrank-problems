#!/bin/python3

import sys


https://www.hackerrank.com/challenges/staircase/problem


n = int(input().strip())

def stair_func(y):
    iter8t = 0
    hshtg = 0
    for x in range(0,y):
        
        iter8t = iter8t + 1
        hshtg = hshtg + 1
    
        for x in range(0,y-iter8t):
            print(' ', end='')
        
        for x in range(0,hshtg):
            print('#', end = '')
        print("")

stair_func(n)
    
