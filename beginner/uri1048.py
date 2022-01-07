# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 19:27:56 2022

@author: camila

Salary Increase

The company ABC decided to give a salary increase to its employees, according to the following table:

Salary	                   Readjustment Rate
0 - 400.00                 15%
400.01 - 800.00            12%
800.01 - 1200.00           10%
1200.01 - 2000.00          7%
Above 2000.00              4%

Read the employee's salary, calculate and print the new employee's salary, as well the money earned and the increase percentual obtained by the employee, with corresponding messages in Portuguese, as the below example.
Input
The input contains only a floating-point number, with 2 digits after the decimal point.

Output
Print 3 messages followed by the corresponding numbers (see example) informing the new salary, the among of money earned and the percentual obtained by the employee. Note:
Novo salario:  means "New Salary"
Reajuste ganho: means "Money earned"
Em percentual: means "In percentage"
"""

salary = float(input())

a = 0.15
b = 0.12
c = 0.1
d = 0.07
e = 0.04

if (salary > 0) and (salary <= 400.00):
    moneyEarned = salary * a
    newSalary = salary + moneyEarned
    print('Novo salario: {:.2f}'.format(newSalary))
    print('Reajuste ganho: {:.2f}'.format(moneyEarned))
    print('Em percentual: 15 %')
elif (salary > 400.00) and (salary <= 800.00):
    moneyEarned = salary * b
    newSalary = salary + moneyEarned
    print('Novo salario: {:.2f}'.format(newSalary))
    print('Reajuste ganho: {:.2f}'.format(moneyEarned))
    print('Em percentual: 12 %')
elif (salary > 800.00) and (salary <= 1200.00):
    moneyEarned = salary * c
    newSalary = salary + moneyEarned
    print('Novo salario: {:.2f}'.format(newSalary))
    print('Reajuste ganho: {:.2f}'.format(moneyEarned))
    print('Em percentual: 10 %')
elif (salary > 1200.00) and (salary <= 2000.00):
    moneyEarned = salary * d
    newSalary = salary + moneyEarned
    print('Novo salario: {:.2f}'.format(newSalary))
    print('Reajuste ganho: {:.2f}'.format(moneyEarned))
    print('Em percentual: 7 %')
else:
    moneyEarned = salary * e
    newSalary = salary + moneyEarned
    print('Novo salario: {:.2f}'.format(newSalary))
    print('Reajuste ganho: {:.2f}'.format(moneyEarned))
    print('Em percentual: 4 %')
    
    
    