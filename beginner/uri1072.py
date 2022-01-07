# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 02:22:04 2022

@author: camila

Interval 2

Read an integer N. This N will be the number of integer numbers X that will be read.

Print how many these numbers X are in the interval [10,20] and how many values are out of this interval.
 

Input
The first line of input is an integer N (N < 10000), that indicates the total number of test cases.
Each case is an integer number X (-107 < X < 107).

 

Output
For each test case, print how many numbers are in and how many values are out of the interval.
"""

n = int(input())

inside = 0
outside = 0

for i in range(1, n+1):
    x = int(input())
    if x >= 10 and x <= 20:
        inside = inside + 1
    else:
        outside = outside +1

print('{} in'.format(inside))
print('{} out'.format(outside))