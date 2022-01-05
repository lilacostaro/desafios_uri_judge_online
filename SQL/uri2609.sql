"""
Created on Tue Jan  4 21:43:23 2022

@author: camila

Products by Categories

As usual the sales industry is doing an analysis of how many products we have in stock, and you can help them.

Then your job will display the name and amount of products of each category.
"""

SELECT 
    categories.name,
    SUM(products.amount)
FROM products
JOIN categories ON categories.id = products.id_categories
GROUP BY categories.name;