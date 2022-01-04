# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 02:49:33 2021

@author: camil
"""
p1 = input().split(" ")
p2 = input().split(" ")

x1, y1 = p1
x2, y2 = p2

distance = (((float(x2) - float(x1))**2) + ((float(y2) - float(y1))**2)) ** 0.5

print('{:.4f}'.format(distance))
