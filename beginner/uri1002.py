# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 19:21:19 2022

@author: camila

Area of a Circle

The formula to calculate the area of a circumference is defined as A = π . R2. Considering to this problem that π = 3.14159:

Calculate the area using the formula given in the problem description.

Input
The input contains a value of floating point (double precision), that is the variable R.

Output
Present the message "A=" followed by the value of the variable, as in the example bellow, with four places after the decimal point. Use all double precision variables. Like all the problems, don't forget to print the end of line after the result, otherwise you will receive "Presentation Error".
"""

R = float(input())

pi = 3.14159

A = pi * (R**2)

print('A={:.4f}'.format(A))