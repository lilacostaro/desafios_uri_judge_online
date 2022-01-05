# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 03:43:52 2021

@author: camila

Age in Days

Read an integer value corresponding to a person's age (in days) and print it in years, months and days, followed by its respective message “ano(s)”, “mes(es)”, “dia(s)”.

Note: only to facilitate the calculation, consider the whole year with 365 days and 30 days every month. In the cases of test there will never be a situation that allows 12 months and some days, like 360, 363 or 364. This is just an exercise for the purpose of testing simple mathematical reasoning.

Input
The input file contains 1 integer value.

Output
Print the output, like the following example.
"""

age = int(input())

years = age // 365
daysleft = age % 365

months = daysleft // 30
days = daysleft % 30

print('{} ano(s)'.format(years))
print('{} mes(es)'.format(months))
print('{} dia(s)'.format(days))
