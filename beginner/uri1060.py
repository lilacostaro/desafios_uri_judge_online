# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 22:01:19 2022

@author: camila

Positive Numbers

Write a program that reads 6 numbers. These numbers will only be positive or negative (disregard null values). Print the total number of positive numbers.

Input
Six numbers, positive and/or negative.

Output
Print a message with the total number of positive numbers.
"""

n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())

lista = [n1, n2, n3, n4, n5, n6]
count = 0

for number in lista:
    if number > 0:
        count = count + 1
print('{} valores positivos'.format(count))

