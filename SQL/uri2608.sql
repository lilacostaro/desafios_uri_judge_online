"""
Created on Tue Jan  4 21:40:43 2022

@author: camila

Higher and Lower Price

The financial sector of our company, wants to know the smaller and higher values of the products, which we sell.

For this you must display only the highest and lowest price of the products table.
"""

SELECT 
    MAX(price),
    MIN(price)
FROM products;