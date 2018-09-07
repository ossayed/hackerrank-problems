#!/bin/python3

import sys


https://www.hackerrank.com/challenges/birthday-cake-candles/problem


def birthdayCakeCandles(n, ar):
    lrg_cndl_qnty = 0
    # Complete this function
    lrg_cndl = max(ar)
    for x in range(n):
        if ar[x] == lrg_cndl:
            lrg_cndl_qnty = lrg_cndl_qnty + 1
            
    return lrg_cndl_qnty
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
