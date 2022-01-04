# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 03:52:30 2021

@author: camil
"""

n = float(input())

n100 = n // 100
n = n % 100

n50 = n // 50
n = n % 50

n20 = n // 20
n = n % 20

n10 = n // 10
n = n % 10

n5 = n // 5
n = n % 5

n2 = n // 2
n = n % 2

n1 = n // 1
n = n % 1

n050 = n // 0.50
n = n % 0.50

n025 = n // 0.25
n = n % 0.25

n010 = n // 0.10
n = n % 0.10

n005 = n // 0.05
n = n % 0.05

n001 = n // 0.01

print('NOTAS:')
print('{} nota(s) de R$ 100,00'.format(n100))
print('{} nota(s) de R$ 50,00'.format(n50))
print('{} nota(s) de R$ 20,00'.format(n20))
print('{} nota(s) de R$ 10,00'.format(n10))
print('{} nota(s) de R$ 5,00'.format(n5))
print('{} nota(s) de R$ 2,00'.format(n2))
print('MOEDAS:')
print('{} moedas(s) de R$ 1,00'.format(n1))
print('{} moedas(s) de R$ 0,50'.format(n050))
print('{} moedas(s) de R$ 0,25'.format(n025))
print('{} moedas(s) de R$ 0,10'.format(n010))
print('{} moedas(s) de R$ 0,05'.format(n005))
print('{} moedas(s) de R$ 0,01'.format(n001))