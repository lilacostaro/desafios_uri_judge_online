# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 19:38:47 2022

@author: camila

Simple Product

Read two integer values. After this, calculate the product between them and store the result in a variable named PROD. Print the result like the example below. Do not forget to print the end of line after the result, otherwise you will receive “Presentation Error”.

Input
The input file contains 2 integer numbers.

Output
Print the message "PROD" and PROD according to the following example, with a blank space before and after the equal signal.
"""

A = int(input())
B = int(input())

PROD = A * B

print('PROD = {prod}'.format(prod=PROD))