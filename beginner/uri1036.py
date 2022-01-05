# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 23:52:07 2022

@author: camila

Bhaskara's Formula

Read 3 floating-point numbers. After, print the roots of bhaskara’s formula. If it's impossible to calculate the roots because a division by zero or a square root of a negative number, presents the message “Impossivel calcular”.

Input
Read 3 floating-point numbers (double) A, B and C.

Output
Print the result with 5 digits after the decimal point or the message if it is impossible to calculate.
"""

numbers = input().split(' ')

A, B, C = numbers

a = float(A)
b = float(B)
c = float(C)

delta = (b ** 2) - (4 * a * c)

if (a == 0) or (delta < 0):
    print('Impossivel calcular')
else:
    x1 = ((-b) + (delta ** 0.5)) / (2 * a)
    x2 = ((-b) - (delta ** 0.5)) / (2 * a)
    print('R1 = {:.5f}'.format(x1))
    print('R2 = {:.5f}'.format(x2))