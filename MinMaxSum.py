#!/bin/python3

import os
import sys

#
# Complete the miniMaxSum function below.
#
def miniMaxSum(arr):
    m = min(arr)
    M = max(arr)
    s = 0
    for num in arr:
        s = s + num
        
    print(s-M,s-m)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
