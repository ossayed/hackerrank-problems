#!/bin/python3

import os
import sys


#https://www.hackerrank.com/challenges/apple-and-orange/problem


def countApplesAndOranges(s, t, a, b, apples, oranges):
    #
    # Write your code here.
    #
    nmbr_fln_appls = 0
    nmbr_fln_orngs = 0
    fln_frts = m + n
    for x in range(0,m):
        frt_pos= a + apples[x]
        if s<= frt_pos <=t:
            nmbr_fln_appls = nmbr_fln_appls + 1
        if x == m-1: 
            print(nmbr_fln_appls)
            
    for x in range(0,n):
        frt_pos= b + oranges[x]
        if s<= frt_pos <=t:
            nmbr_fln_orngs = nmbr_fln_orngs + 1
        if x == n-1: 
            print(nmbr_fln_orngs)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apple = list(map(int, input().rstrip().split()))

    orange = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apple, orange)