#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    l=len(ar)
    j=0
    max=ar[0]
    for i in range (1,l):
        if ar[i]>max:
            max=ar[i]
    for i in range (0,l):
        if max==ar[i]:
            j+=1        
    return j
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
