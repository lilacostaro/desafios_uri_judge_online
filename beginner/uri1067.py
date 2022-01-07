# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 01:46:02 2022

@author: camila

Odd Numbers

Read an integer value X (1 <= X <= 1000).  Then print the odd numbers from 1 to X, each one in a line, including X if is the case.

Input
The input will be an integer value.

Output
Print all odd values between 1 and X, including X if is the case.
"""

x = int(input())

if (x >= 1) and (x <= 1000):
    for x in range(1, x+1):
        if (x % 2) != 0:
            print(x)