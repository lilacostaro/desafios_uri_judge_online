# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 00:06:12 2022

@author: camila

Snack

Using the following table, write a program that reads a code and the amount of an item. After, print the value to pay. This is a very simple program with the only intention of practice of selection commands.

Input
The input file contains two integer numbers X and Y. X is the product code and Y is the quantity of this item according to the above table.

Output
The output must be a message "Total: R$ " followed by the total value to be paid, with 2 digits after the decimal point.
"""

order = input().split(' ')

X, Y = order
x = int(X)
y = int(Y)

a = 4.00
b = 4.50
c = 5.00
d = 2.00
e = 1.50

if x == 1:
    value = y * a
    print('Total: R$ {:.2f}'.format(value))
elif x == 2:
    value = y * b
    print('Total: R$ {:.2f}'.format(value))
elif x == 3:
    value = y * c
    print('Total: R$ {:.2f}'.format(value))
elif x == 4:
    value = y * d
    print('Total: R$ {:.2f}'.format(value))
elif x == 5:
    value = y * e
    print('Total: R$ {:.2f}'.format(value))