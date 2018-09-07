#!/bin/python3

import os
import sys


#https://www.hackerrank.com/challenges/grading/problem


def gradingStudents(grades):
    grades_new = []
    for x in range(0,n):      
        list_str = list(str(grades[x]))
        if grades[x] < 38:
            grades_new.append(grades[x])
        elif "3" <= str(list_str[1]) <= "5":
            list_str[1] = "5"
            grade ="".join(str(v) for v in list_str)
            grades_new.append(grade)
            
        elif str(list_str[1]) >="8"  :
            list_str[0] = int(list_str[0]) + 1  
            (list_str[1]) = "0"
            grade ="".join(str(v) for v in list_str)
            grades_new.append(grade)
               
        else:
            grade ="".join(str(v) for v in list_str)
            grades_new.append(grade)

    return(grades_new)
            
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()