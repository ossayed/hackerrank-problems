#!/bin/python3

import os
import sys


#https://www.hackerrank.com/challenges/between-two-sets/problem


def getTotalX(a, b):
    #
    # Write your code here.
    #
    pot_factors = []
    factors = []
    
    for x in range(1,min(b) + 1):
        factor_0 = 0
        for y in range(0,n):
            if x % a[y] == 0:
                factor_0 = factor_0 + 1
                
            if factor_0 == n:
                pot_factors.append(x)
    
    for x in range(0,len(pot_factors)):
        factor_1 = 0
        for y in range(0,m):
            if b[y] % pot_factors[x] == 0:
                factor_1 = factor_1 + 1
                
            if factor_1 == m:
                
                factors.append(pot_factors[x])
                
    return(len(factors))
            

                
                
            
                
                
        
        
                
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
