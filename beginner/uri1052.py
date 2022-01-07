# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 21:30:59 2022

@author: camila

Month

Read an integer number between 1 and 12, including. Corresponding to this number, you must print the month of the year, in english, with the first letter in uppercase.

Input
The input contains only an integer number.

Output
Print the name of the month according to the input number, with the first letter in uppercase.
"""

month = int(input())

months = {
    'January': 1, 
    'February': 2, 
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
    }

if (month >= 1) and (month <= 12):
    def get_key(month):
        for key, value in months.items():
            if month ==  value:
                return key
        return 'DDD nao cadastrado'
    
    print(get_key(month))
    
else:
    print('Invalid Month')