#Given a square matrix, calculate the absolute difference between the sums of its diagonals.

#For example, the square matrix arr is shown below:
#1 2 3
#4 5 6
#9 8 9

#The left-to-right diagonal = 1+5+9 = 15
#The right to left diagonal = 3+5+9=17
#Their absolute difference is |15-17| = 2.

#Function Description:
#Complete the diagonalDifference function in the editor below.

#diagonalDifference takes the following parameter:
#int arr[n][m]: an array of integers

#Returns:
#int: the absolute diagonal difference

#Input Format
#The first line contains a single integer, n, the number of rows and columns in the square matrix arr.

#Each of the next n lines describes a row, arr[i],
#and consists of n space-separated integers arr[i][j].

#Output Format
#Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

#Sample Input
#3
#11 2 4
#4 5 6
#10 8 -12

#Sample Outout:
#15

#Explanation:

#The primary diagonal is:
#11
#  5
#   -12
#Sum across the primary diagonal: 11 + 5 - 12 = 4

#The secondary diagonal is:
#     4
#   5
#10
#Sum across the secondary diagonal: 4 + 5 + 10 = 19

#Difference: |4 - 19| = 15

#Code:
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    diag_1, diag_2, n = 0,0, len(arr)
    
    # index i and j to access indeces of the matrix
    for i in range(0,n):
        for j in range(0,n):
            
            #for diag_1, values to be added at arr[i][j]
            if i == j:
                diag_1 += arr[i][j]
                
            #for diag_2, we go the opposite direction
            if i == (n-j-1):
                diag_2 += arr[i][j]
                
    #now, we simply return the absolute value of the difference between the two
    return abs(diag_1 - diag_2)
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()