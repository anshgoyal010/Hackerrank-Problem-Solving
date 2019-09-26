#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the almostSorted function below.
def almostSorted(arr):
    a=arr
    f=0
    if arr==sorted(arr):
        print("yes")
    else:
        #arr[x:y]=reversed(arr[x:y])
        for i in range(0,len(arr)-1):
            if arr[i+1]<arr[i]:
                temp2=arr.index(min(arr[i+1:]))
                arr[temp2],arr[i]=arr[i],arr[temp2]
                break
        if arr==sorted(arr):
            print("yes")
            print("swap "+str(i+1)+" "+str(temp2+1))
        else:
            arr[temp2],arr[i]=arr[i],arr[temp2]
            for i in range(0,len(arr)-1):
                if arr[i+1]<arr[i]:
                    n=arr[i]
                    x=i
                    break
            for i in range(x+1,len(arr)):
                if arr[i]>n:
                    y=i
                    f=1
                    break
            if f==0:
                y=len(arr)-1
            arr[x:y]=reversed(arr[x:y])
            if arr==sorted(arr):
                print("yes")
                print("reverse "+str(x+1)+" "+str(y))
            else:
                print("no")

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
