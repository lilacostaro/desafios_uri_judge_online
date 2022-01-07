# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 02:05:18 2022

@author: camila

Sum of Consecutive Odd Numbers I

Read two integer values X and Y. Print the sum of all odd values between them.

Input
The input file contain two integer values.

Output
The program must print an integer number. This number is the sum off all odd values between both input values that must fit in an integer number.
"""

x = int(input())
y = int(input())

lista = []

if x >= y:
    for a in range(y+1, x):
        if (a % 2) != 0:
            lista.append(a)
else:
    for a in range(x+1, y):
        if (a % 2) != 0:
            lista.append(a)

print(sum(lista))