#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    x=len(s)
    y=len(t)
    if x+y<=k:
        return "Yes"
    elif s==t:
        if k%2==0:
            return "Yes"
        else:
            return "No"
    else:        
        for i in range(0,min(x,y)):
            a=s[i]
            b=t[i]
            if a!=b:
                break
        if (len(s[i:])+len(t[i:])-k)%2==0 and (len(s[i:])+len(t[i:]))<=k:
            return "Yes"
        else:
            return "No"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
