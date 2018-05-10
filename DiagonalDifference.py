#!/bin/python3

import os
import sys


def diagonalDifference(a):
    d1 = sum([a[x][x] for x in range(n)]) 
    d2 = sum([a[x][n-1-x] for x in range (n)])
    return(abs(d1-d2))   

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    f.write(str(result) + '\n')

    f.close()
