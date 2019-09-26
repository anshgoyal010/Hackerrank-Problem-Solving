#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    l=len(a)
    z=[]
    for i in range(0,l):
        a.append(a[i])
        x=a.index(a[i],i+1,l+1)
        del a[l]
        if x!=l:
            z.append(x-i)
    if len(z)>0:
        return min(z)
    else:
        return -1



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
