#!/bin/python3

import sys


#https://www.hackerrank.com/challenges/compare-the-triplets/problem


a0,a1,a2 = input().strip().split(' ')
alice_list = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
bob_list = [int(b0),int(b1),int(b2)]
def point_find():
    alice_points = 0
    bob_points = 0
    for i in range(len(alice_list)):
        if (alice_list[i] > bob_list[i]):
            alice_points = alice_points + 1
            
        if(bob_list[i] > alice_list[i]):
            bob_points = bob_points + 1
            
    print(alice_points,bob_points)  
    
    
point_find()