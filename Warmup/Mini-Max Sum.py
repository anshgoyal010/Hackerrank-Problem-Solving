#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    l=len(arr)
    max=arr[0]
    min=arr[0]
    s=arr[0]
    for i in range (1,l):
        s+=arr[i]
        if arr[i]>max:
            max=arr[i]
        if arr[i]<min:
            min=arr[i]
    print((s-max),(s-min))         
        

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
