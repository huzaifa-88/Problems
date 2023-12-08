#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # 1st Method
    sumArr = []
    for i in range(len(arr) - 1, -1, -1):
        originalArr = arr.copy()
        originalArr.remove(originalArr[i])
        mySum = sum(originalArr)
        sumArr.append(mySum)
    print(min(sumArr), max(sumArr))
    # 2nd method
    # print(sum(arr) - max(arr), sum(arr) - min(arr))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
