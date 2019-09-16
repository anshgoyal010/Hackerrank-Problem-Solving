#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    lvl=0
    v=0
    for i in range(0,n):
        if s[i]=='U':
            lvl+=1
        else:
            lvl-=1
        if lvl==0 and s[i]=='U':
            v+=1
    return v

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
