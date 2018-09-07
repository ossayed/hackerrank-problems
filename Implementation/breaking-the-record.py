#!/bin/python3

import os
import sys


#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem


def breakingRecords(score):
    #
    # Write your code here.
    #
    high_score = score[0]
    low_score = score[0]
    high_record = 0
    low_record = 0
    for x in range(0,n):
        if score[x] > high_score:
            high_score = score[x]
            high_record = high_record + 1
        
        if score[x] < low_score:
            low_score = score[x]
            low_record = low_record + 1
    
    return(high_record,low_record)
    
            

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    score = list(map(int, input().rstrip().split()))

    result = breakingRecords(score)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()
