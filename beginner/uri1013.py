# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 02:38:29 2021

@author: camila

The Greatest

Make a program that reads 3 integer values and present the greatest one followed by the message "eh o maior". Use the following formula:



Input
The input file contains 3 integer values.

Output
Print the greatest of these three values followed by a space and the message “eh o maior”.
"""

values = input().split(" ")

a, b, c = values

MaiorAB = ((int(a) + int(b)) + abs(int(a) - int(b))) / 2

result = ((int(MaiorAB) + int(c)) + (abs(int(MaiorAB) - int(c)))) / 2

print('{} eh o maior'.format(int(result)))