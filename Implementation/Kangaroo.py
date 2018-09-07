#!/bin/python3

import sys


#https://www.hackerrank.com/challenges/kangaroo/problem


def kangaroo(x1, v1, x2, v2):
    num = x2 - x1
    den = v1 - v2
    if den == 0:
        return 'YES' if num == 0 else 'NO'
    return 'YES' if (num / den > 0 and num % den == 0) else 'NO'

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
