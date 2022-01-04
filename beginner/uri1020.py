# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 03:43:52 2021

@author: camil
"""

age = int(input())

years = age // 365
daysleft = age % 365

months = daysleft // 30
days = daysleft % 30

print('{} ano(s)'.format(years))
print('{} mes(es)'.format(months))
print('{} dia(s)'.format(days))
