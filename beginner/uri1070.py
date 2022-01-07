# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 01:55:59 2022

@author: camila

Six Odd Numbers

Read an integer value X and print the 6 consecutive odd numbers from X, a value per line, including X if it is the case.

Input
The input will be a positive integer value.

Output
The output will be a sequence of six odd numbers.
"""

x = int(input())

if x > 0:
    for number in range(x, x+12):
        if (number % 2) != 0:
            print(number)