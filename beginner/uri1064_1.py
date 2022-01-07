# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 23:15:08 2022

@author: camila

Positives and Average

Read 6 values that can be floating point numbers. After, print how many of them were positive. In the next line, print the average of all positive values typed, with one digit after the decimal point.

Input
The input consist in 6 numbers that can be integer or floating point values. At least one number will be positive.

Output
The first output value is the amount of positive numbers. The next line should show the average of the positive values ​typed.
"""

n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())

lista = [n1, n2, n3, n4, n5, n6]

count = 0
sum_values = 0

for number in lista:
    if number > 0:
        count = count + 1
print('{} valores positivos'.format(count))

for number in lista:
    if number >= 0:
        sum_values += number
avg = sum_values / count
print('{:.1f}'.format(avg))