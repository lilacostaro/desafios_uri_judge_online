"""
Created on Tue Jan  4 22:19:26 2022

@author: camila

Simple Calculate

In this problem, the task is to read a code of a product 1, the number of units of product 1, the price for one unit of product 1, the code of a product 2, the number of units of product 2 and the price for one unit of product 2. After this, calculate and show the amount to be paid.

Input
The input file contains two lines of data. In each line there will be 3 values: two integers and a floating value with 2 digits after the decimal point.

Output
The output file must be a message like the following example where "Valor a pagar" means Value to Pay. Remember the space after ":" and after "R$" symbol. The value must be presented with 2 digits after the point.
"""

product1 = input().split(' ')
product2 = input().split(' ')

a, b, c = product1
d, e, f = product2

total1 = int(b) * float(c)
total2 = int(e) * float(f)
total = total1 + total2

print('VALOR A PAGAR: R$ {:.2f}'.format(total))