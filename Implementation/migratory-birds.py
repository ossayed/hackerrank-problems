#!/bin/python3

import sys


#https://www.hackerrank.com/challenges/migratory-birds/problem


def migratoryBirds(n, ar):
    # Complete this function
    bird0 = 0
    bird1 = 0
    bird2 = 0
    bird3 = 0
    bird4 = 0
    max_index = 0
    
    for x in range(0,n):
        if ar[x] == 1:
            bird0 = bird0 + 1
            #print("hello")
            bird0_tup = (bird0,1)
        elif ar[x] == 2:
            bird1 = bird1 + 1
            bird1_tup = (bird1,2)
        elif ar[x] == 3:
            bird2 = bird2 + 1
            bird2_tup = (bird2,3);
        elif ar[x] == 4:
            bird3 = bird3 + 1
            bird3_tup = (bird3,4); 
        else:
            bird4 = bird4 + 1
            bird4_tup = (bird4,5);
    
    
    #bird_qnty = [bird0_tup,bird1_tup,bird2_tup,bird3_tup,bird4_tup]
    bird_qnty = [bird0,bird1,bird2,bird3,bird4]
    max_value = max(bird_qnty)
    max_index = bird_qnty.index(max_value)
    return(max_index + 1)


    #for y in range(0,len(bird_qnty)):
       #max_value = bird_qnty[0]
        #if bird_qnty[y] > max_value:
          #  max_value = bird_qnty[y]
           # max_index = y + 1
    #return(max_index)
            
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
