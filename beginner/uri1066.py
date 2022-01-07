# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 01:29:47 2022

@author: camila

Even, Odd, Positive and Negative

Make a program that reads five integer values. Count how many   of these values are even, odd, positive and negative. Print these information like following example.

Input
The input will be 5 integer values.

Output
Print a message like the following example with all letters in lowercase, indicating how many of these values ​​are even, odd, positive and negative.
"""

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

lista = [n1, n2, n3, n4, n5]

count_even = 0
count_odd = 0
count_positive = 0
count_negative = 0
for number in lista:
    if (number % 2) == 0:
        count_even += 1
    else:
        count_odd += 1
for number in lista:
    if number > 0:
        count_positive += 1
    elif number < 0:
        count_negative += 1
print('{} valor(es) par(es)'.format(count_even))
print('{} valor(es) impar(es)'.format(count_odd))
print('{} valor(es) positivo(s)'.format(count_positive))
print('{} valor(es) negativo(s)'.format(count_negative))