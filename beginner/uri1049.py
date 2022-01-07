# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 19:55:57 2022

@author: camila

Animal

Input
The input contains 3 words, one by line, that will be used to identify the animal, according to the above table, with all letters in lowercase.

Output
Print the animal name according to the given input.
"""
h1 = input()
h2 = input()
h3 = input()

if h1 == 'vertebrado':
    if h2 == 'ave':
        if h3 == 'carnivoro':
            print('aguia')
        if h3 == 'onivoro':
            print('pomba')
    if h2 == 'mamifero':
        if h3 == 'herbivoro':
            print('vaca')
        if h3 == 'onivoro':
            print('homem')

if h1 == 'invertebrado':
    if h2 == 'inseto':
        if h3 == 'hematofago':
            print('pulga')
        elif h3 == 'herbivoro':
            print('lagarta')
    if h2 == 'anelideo':
        if h3 == 'hematofago':
            print('sanguessuga')
        if h3 == 'onivoro':
            print('minhoca')
