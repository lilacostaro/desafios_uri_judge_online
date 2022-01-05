# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 02:55:28 2022

@author: camila

Multiples

Read two nteger values (A and B). After, the program should print the message "Sao Multiplos" (are multiples) or "Nao sao Multiplos" (aren’t multiples), corresponding to the read values.

Input
The input has two integer numbers.

Output
Print the relative message to the input as stated above.
"""

values = input().split(' ')

A, B = values
a = int(A)
b = int(B)

m = b % a
n = a % b

if b > a:
    if m == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')

elif a == b:
    print('Sao Multiplos')
        
else:
    if n == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')