#!/bin/python3

import math
import os
import random
import re
import sys
import math
# Complete the squares function below.
def squares(a, b):
    c=0
    while(a<b+1):
        if math.sqrt(a)==int(math.sqrt(a)):
            c+=1
            a=a+(2*math.sqrt(a))
        a+=1
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
