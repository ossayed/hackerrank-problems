#!/bin/python3

import sys


#https://www.hackerrank.com/challenges/the-birthday-bar/problem


def solve(n, s, d, m):
    # Complete this function
    num_sol = 0
    y = 0
    pot_sol = 0
    #if n == 1 and m ==1:
        #return(m)
    for x in range(0,n-(m-1)):
        #ot_sol = 0
        for y in range(0,m):
            pot_sol = pot_sol + s[x + y]
            #print(pot_sol)
        y = y + 1
        if pot_sol == d:
            num_sol = num_sol + 1
        if y == m:
            pot_sol = 0
    
    return(num_sol)
                
            
n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
