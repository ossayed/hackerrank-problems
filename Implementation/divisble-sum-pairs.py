#!/bin/python3

import sys


#https://www.hackerrank.com/challenges/divisible-sum-pairs/problem


def divisibleSumPairs(n, k, ar):
    # Complete this function
    num_sol = 0 
    for x in range(0,n):
        for y in range(1,n-x):
            pot_sol = 0
            pot_sol = ar[x] + ar[x + y]
            #print(pot_sol)
            if pot_sol % k == 0:
                num_sol = num_sol + 1
                
    return(num_sol)
            
if __name__ == '__main__':
            
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    ar = list(map(int, input().strip().split(' ')))
    result = divisibleSumPairs(n, k, ar)
    print(result)