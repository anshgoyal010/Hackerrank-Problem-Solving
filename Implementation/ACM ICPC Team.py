#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    n=[]
    for i in range(0,len(topic)):
        n.append(i)
    from itertools import combinations
    li=list(combinations(n,2))
    l=[]
    for i in li:
        a=(int(topic[int(i[0])])+int(topic[int(i[1])]))
        b=(len(topic[0])-len(str(a)))
        l.append(len(topic[0])-(str(a).count('0'))-b)
    a=[max(l),l.count(max(l))]
    return a
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
