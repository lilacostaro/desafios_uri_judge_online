"""
Created on Tue Jan  4 21:55:35 2022

@author: camila

Average Value of Products

In the company that you work is being done a survey on the values of the products that are marketed.

To help the industry that is doing this survey you should calculate and display the average value of the price of the products.

OBS: Show the value with two numbers after the period.
"""

SELECT ROUND(AVG(price), 2) FROM products;