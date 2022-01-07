# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 18:52:00 2022

@author: camila

Game Time

Read the start time and end time of a game, in hours. Then calculate the duration of the game, knowing that the game can begin in a day and finish in another day, with a maximum duration of 24 hours. The message must be printed in portuguese “O JOGO DUROU X HORA(S)” that means “THE GAME LASTED X HOUR(S)”

Input
Two integer numbers representing the start and end time of a game.

Output
Print the duration of the game as in the sample output.
"""

time = input().split(' ')

X, Y = time
x = int(X)
y = int(Y)

if y > x:
    hours = y - x
    print('O JOGO DUROU {} HORA(S)'.format(hours))
else:
    hours1 = 24 - x
    hours2 = 0 + y
    hours = hours1 + hours2
    print('O JOGO DUROU {} HORA(S)'.format(hours))
    