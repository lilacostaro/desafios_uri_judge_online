# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 23:33:50 2022

@author: camila

Even Between five Numbers

Make a program that reads five integer values. Count how many of these values ​​are even and  print this information like the following example.

Input
The input will be 5 integer values.

Output
Print a message like the following example with all letters in lowercase, indicating how many even numbers were typed.
"""

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

lista = [n1, n2, n3, n4, n5]

count = 0
for number in lista:
    if (number % 2) == 0:
        count += 1
print('{} valores pares'.format(count))