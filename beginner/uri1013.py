# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 02:38:29 2021

@author: camil
"""

values = input().split(" ")

a, b, c = values

MaiorAB = ((int(a) + int(b)) + abs(int(a) - int(b))) / 2

result = ((int(MaiorAB) + int(c)) + (abs(int(MaiorAB) - int(c)))) / 2

print('{} eh o maior'.format(int(result)))