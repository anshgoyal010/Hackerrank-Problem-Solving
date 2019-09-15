#!/bin/python3

import math
import os
import random
import re
import sys
import array

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    l=len(a)
    arr = array.array('i',[0,0])
    for i in range (0,l):
        if(a[i]>b[i]):
            arr[0]=arr[0]+1
        if(a[i]<b[i]):    
            arr[1]=arr[1]+1
    return arr    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
