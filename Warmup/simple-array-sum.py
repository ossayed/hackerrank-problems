#!/bin/python3

import sys


# https://www.hackerrank.com/challenges/simple-array-sum/problem


def array_sum(n, arr):
    sum = 0
    for i in range(n):
        sum = sum + arr[i]
    print(sum)


if __name__ == '__main__':
	n = int(input().strip())
	arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
	array_sum()