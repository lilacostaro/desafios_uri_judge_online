# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 20:26:49 2022

@author: camila

DDD

Read an integer number that is the code number for phone dialing. Then, print the destination according to the following table:

https://resources.beecrowd.com.br/gallery/images/problems/UOJ_1050.png


If the input number isn’t found in the above table, the output must be:
DDD nao cadastrado
That means “DDD not found” in Portuguese language.

Input
The input consists in a unique integer number.

Output
Print the city name corresponding to the input DDD. Print DDD nao cadastrado if doesn't exist corresponding DDD to the typed number.
"""

ddd = int(input())

cidades = {
    'Brasilia': 61, 
    'Salvador': 71, 
    'Sao Paulo': 11,
    'Rio de Janeiro': 21,
    'Juiz de Fora': 32,
    'Campinas': 19,
    'Vitoria': 27,
    'Belo Horizonte': 31
    }

def get_key(ddd):
    for key, value in cidades.items():
        if ddd ==  value:
            return key
    return 'DDD nao cadastrado'

print(get_key(ddd))
