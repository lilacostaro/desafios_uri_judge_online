# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 03:52:30 2021

@author: camila

Banknotes and Coins

Read a value of floating point with two decimal places. This represents a monetary value. After this, calculate the smallest possible number of notes and coins on which the value can be decomposed. The considered notes are of 100, 50, 20, 10, 5, 2. The possible coins are of 1, 0.50, 0.25, 0.10, 0.05 and 0.01. Print the message “NOTAS:” followed by the list of notes and the message “MOEDAS:” followed by the list of coins.

Input
The input file contains a value of floating point N (0 ≤ N ≤ 1000000.00).

Output
Print the minimum quantity of banknotes and coins necessary to change the initial value, as the given example.
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
print('{} nota(s) de R$ 100.00'.format(int(n100)))
print('{} nota(s) de R$ 50.00'.format(int(n50)))
print('{} nota(s) de R$ 20.00'.format(int(n20)))
print('{} nota(s) de R$ 10.00'.format(int(n10)))
print('{} nota(s) de R$ 5.00'.format(int(n5)))
print('{} nota(s) de R$ 2.00'.format(int(n2)))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(int(n1)))
print('{} moeda(s) de R$ 0.50'.format(int(n050)))
print('{} moeda(s) de R$ 0.25'.format(int(n025)))
print('{} moeda(s) de R$ 0.10'.format(int(n010)))
print('{} moeda(s) de R$ 0.05'.format(int(n005)))
print('{} moeda(s) de R$ 0.01'.format(int(n001)))