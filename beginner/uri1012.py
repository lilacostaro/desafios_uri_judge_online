# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 02:18:00 2021

@author: camila

Area

Make a program that reads three floating point values: A, B and C. Then, calculate and show:
a) the area of the rectangled triangle that has base A and height C.
b) the area of the radius's circle C. (pi = 3.14159)
c) the area of the trapezium which has A and B by base, and C by height.
d) the area of ​​the square that has side B.
e) the area of the rectangle that has sides A and B.

Input
The input file contains three double values with one digit after the decimal point.

Output
The output file must contain 5 lines of data. Each line corresponds to one of the areas described above, always with a corresponding message (in Portuguese) and one space between the two points and the value. The value calculated must be presented with 3 digits after the decimal point.
"""

valor = input().split(" ")
a, b, c = valor
pi = 3.14159

triRet = (float(a) * float(c)) / 2
circle = pi * (float(c) ** 2)
trapezium = ((float(a) + float(b)) * float(c)) / 2
square = float(b) ** 2
rectangle = float(a) * float(b)

print('TRIANGULO: {:.3f}'.format(triRet))
print('CIRCULO: {:.3f}'.format(circle))
print('TRAPEZIO: {:.3f}'.format(trapezium))
print('QUADRADO: {:.3f}'.format(square))
print('RETANGULO: {:.3f}'.format(rectangle))