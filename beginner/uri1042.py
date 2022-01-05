# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 01:50:02 2022

@author: camila

Simple Sort

Read three integers and sort them in ascending order. After, print these values in ascending order, a blank line and then the values in the sequence as they were readed.

Input
The input contains three integer numbers.

Output
Present the output as requested above.
"""

values = input().split(' ')


a, b, c = values
x = int(a)
y = int(b)
z = int(c)

lista = [x, y, z]

lista.sort()

print(lista[0])
print(lista[1])
print(lista[2])
print(' ')
print(x)
print(y)
print(z)


