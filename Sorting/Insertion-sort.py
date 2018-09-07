#!/bin/python3

import sys


#https://www.hackerrank.com/challenges/insertionsort2/problem


def insertionSort2(n, arr):
    # Complete this function
    for x in range(1,n):
        sort_num = arr[x]
        for y in range(1,x + 1):
            if sort_num < arr[x-y]:
                arr[(x-y)+1] =  arr[x-y]
                arr[(x-y)] = sort_num 
                #print(arr,"a")
            
            if sort_num > arr[x-y]:
                arr[(x-y)+1]= sort_num
                #print(arr,"b")
                break
        arr_str =" ".join(str(v) for v in arr)

        print(arr_str)
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort2(n, arr)
