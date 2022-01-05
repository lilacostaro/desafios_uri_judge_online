# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 02:28:35 2022

@author: camila

Triangle

Read three point floating values (A, B and C) and verify if is possible to make a triangle with them. If it is possible, calculate the perimeter of the triangle and print the message:


Perimetro = XX.X


If it is not possible, calculate the area of the trapezium which basis A and B and C as height, and print the message:


Area = XX.X

Input
The input file has tree floating point numbers.

Output
Print the result with one digit after the decimal point.
"""

medidas = input().split(' ')

a, b, c = medidas

x = float(a)
y = float(b)
z = float(c)

xy = x + y
yz = y + z
zx = z + x

if (xy > z) and (yz > x) and (zx > y):
    perimeter = x + y + z 
    print('Perimetro = {:.1f}'.format(perimeter))
else:
    area = (x + y) / 2 * z
    print('Area = {:.1f}'.format(area))

