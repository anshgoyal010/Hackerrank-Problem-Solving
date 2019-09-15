#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range (0,n):
        for j in range (i,(n-1)):
            print(" ",end='')
        for k in range ((n-i-1),n):
            print("#",end='')
        print()        

if __name__ == '__main__':
    n = int(input())

    staircase(n)
