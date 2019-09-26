#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    e=100
    l=len(c)
    ni=(n+k)%l
    while(ni!=0):
        if c[ni]==1:
            e-=2
        e-=1
        ni=(ni+k)%l
    if c[0]==0:
        return e-1
    else:
        return e-3
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
