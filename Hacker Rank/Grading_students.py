#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    test_grades = grades.copy()
    for i in range(len(grades)):
        if (test_grades[i] % 5 == 4):
            test_grades[i] = test_grades[i] + 1
        elif (test_grades[i] % 5 == 3):
            test_grades[i] = test_grades[i] + 2
        # print(test_grades[i] % 5)
        if (test_grades[i] < 40):
            continue
        if test_grades[i] % 5 == 0 and test_grades[i] >= 40:
            grades[i] = test_grades[i]
    return grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
