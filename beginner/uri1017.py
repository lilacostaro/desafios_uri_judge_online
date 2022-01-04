# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 03:15:29 2021

@author: camil
"""

timeSpent = int(input())
avgSpeed = int(input())

efficiency = 12

distance = timeSpent * avgSpeed
gasNeed = distance/efficiency

print('{:.3f}'.format(gasNeed))