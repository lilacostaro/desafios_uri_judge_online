# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 02:18:00 2021

@author: camil
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