#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    l=len(arr)
    p=0
    z=0
    n=0
    for i in range(0,l):
        if arr[i]>0:
            p+=1
        if arr[i]==0:
            z+=1
        if arr[i]<0:
            n+=1
    p=p/l
    z=z/l
    n=n/l
    print("{:.6f}".format(p))
    print("{:.6f}".format(n))
    print("{:.6f}".format(z))            
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
