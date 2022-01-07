# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 20:17:42 2022

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

if ddd == 61:
    print('Brasilia')
elif ddd == 71:
    print('Salvador')
elif ddd == 11:
    print('Sao Paulo')
elif ddd == 21:
    print('Rio de Janeiro')
elif ddd == 32:
    print('Juiz de Fora')
elif ddd == 19:
    print('Campinas')
elif ddd == 27:
    print('Vitoria')
elif ddd == 31:
    print('Belo Horizonte')
else:
    print('DDD nao cadastrado')
    
    
    
    
    