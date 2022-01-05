# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 23:28:14 2022

@author: camila

Selection Test 1

Read 4 integer values A, B, C and D. Then if B is greater than C and D is greater than A and if the sum of C and D is greater than the sum of A and B and if C and D were positives values and if A is even, write the message “Valores aceitos” (Accepted values). Otherwise, write the message “Valores nao aceitos” (Values not accepted).

Input
Four integer numbers A, B, C and D.

Output
Show the corresponding message after the validation of the values​​.
"""

numbers = input().split(' ')

A, B, C, D = numbers

a = int(A)
b = int(B)
c = int(C)
d = int(D)
sumab = a + b
sumcd = c + d
v1 = a%2

if (b > c) and (d > a) and (sumcd > sumab) and (c >= 0) and (d >= 0) and (v1 == 0):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')