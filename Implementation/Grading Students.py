#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    g=[]
    l=len(grades)
    for i in range(0,l):
        j=grades[i]
        if j>=38:
            if (j%5)==0:
                g.append(j)
            elif (j+1)%5==0:
                j=j+1
                g.append(j)
            elif (j+2)%5==0:
                j=j+2
                g.append(j)
            else:
                g.append(j)                
        if j<38:
            g.append(j)        
    return g


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
