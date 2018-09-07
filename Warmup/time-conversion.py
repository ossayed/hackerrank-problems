#!/bin/python3

import sys


#https://www.hackerrank.com/challenges/time-conversion/problem


def timeConversion(s):
    
    # Complete this function
    if "AM" in s and int(s[:2]) == 12:
        s = s.replace("AM", "")
        s = s.replace(s[:2],"00")
        return(s)

        
        
    if "AM" in s:
        s = s.replace("AM", "")
        return(s)
     
    if int(s[:2]) == 12:
        s = s.replace("PM", "")
        return(s)
    
    else:
        hour = int(s[:2]) + 12
        s = s.replace(s[:2],str(hour))
        s = s.replace("PM", "")
        return(s)

     
        
        
    
s = input().strip()
result = timeConversion(s)
print(result)
