# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 21:09:25 2022

@author: camila

Taxes

In an imaginary country called Lisarb, all the people are very happy to pay their taxes because they know that doesn’t exist corrupt politicians and the taxes are used to benefit the population, without any misappropriation. The currency of this country is Rombus, whose symbol is R$.

Read a value with 2 digits after the decimal point, equivalent to the salary of a Lisarb inhabitant. Then print the due value that this person must pay of taxes, according to the table below.
https://resources.beecrowd.com.br/gallery/images/problems/UOJ_1051_en.png

Remember, if the salary is R$ 3,002.00 for example, the rate of 8% is only over R$ 1,000.00, because the salary from R$ 0.00 to R$ 2,000.00 is tax free. In the follow example, the total rate is 8% over R$ 1000.00 + 18% over R$ 2.00, resulting in R$ 80.36 at all. The answer must be printed with 2 digits after the decimal point.

Input
The input contains only a float-point number, with 2 digits after the decimal point.

Output
Print the message "R$" followed by a blank space and the total tax to be payed, with two digits after the decimal point. If the value is up to 2000, print the message "Isento".
"""

salary = float(input())

if (salary >= 0.00) and (salary <= 2000.00):
    print('Isento')
elif (salary > 2000.00) and (salary <= 3000.00):
    value = salary - 2000
    taxes = value * 0.08
    print('R$ {:.2f}'.format(taxes))
elif (salary > 3000.00) and (salary <= 4500.00):
    value = salary - 3000
    taxes1 = value * 0.18
    taxes2 = 1000 * 0.08
    taxes = taxes1 + taxes2
    print('R$ {:.2f}'.format(taxes))
else:
    value = salary - 4500
    taxes1 = value * 0.28
    taxes2 = 1500 * 0.18
    taxes3 = 1000 * 0.08
    taxes = taxes1 + taxes2 + taxes3
    print('R$ {:.2f}'.format(taxes))