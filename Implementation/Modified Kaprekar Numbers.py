#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    li=[]
    for i in range(p,q+1):
        a=(i*i)%(10**len(str(i)))
        b=(i*i)//(10**len(str(i)))
        if (a+b)==i:
            li.append(i)
    if len(li)>0:
        print(*(sorted(li)))
    else:
        print("INVALID RANGE")


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
