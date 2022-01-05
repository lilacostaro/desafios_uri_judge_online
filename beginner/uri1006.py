# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 19:55:07 2022

@author: camila

Average 2

Read three values (variables A, B and C), which are the three student's grades. Then, calculate the average, considering that grade A has weight 2, grade B has weight 3 and the grade C has weight 5. Consider that each grade can go from 0 to 10.0, always with one decimal place.

Input
The input file contains 3 values of floating points (double) with one digit after the decimal point.

Output
Print the message "MEDIA"(average in Portuguese) and the student's average according to the following example, with a blank space before and after the equal signal.
"""

A = float(input())
B = float(input())
C = float(input())

P1 = 2
P2 = 3
P3 = 5
P = P1 + P2 + P3

while True:
    try:
        if A > 10.0:
            raise InputError('Nota não pode ser maior que 10.')
        elif A < 0:
            raise InputError('Nota não pode ser menor que 0.')
        if B > 10.0:
            raise InputError('Nota não pode ser maior que 10.')
        elif B < 0:
            raise InputError('Nota não pode ser menor que 0.')
        if C > 10.0:
            raise InputError('Nota não pode ser maior que 10.')
        elif C < 0:
            raise InputError('Nota não pode ser menor que 0.')
        avg = ((A * P1) + (B * P2) + (C * P3)) / P
        print('MEDIA = {:.1f}'.format(avg))
        break

    except ValueError:
        print('Valor inválido. Deve-se digitar apenas números.')
    except InputError as ex:
        print(ex)
