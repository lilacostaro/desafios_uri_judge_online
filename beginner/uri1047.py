# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 19:02:15 2022

@author: camila

Game Time with Minutes

Read the start time and end time of a game, in hours and minutes (initial hour, initial minute, final hour, final minute). Then print the duration of the game, knowing that the game can begin in a day and finish in another day,

Obs.: With a maximum game time of 24 hours and the minimum game time of 1 minute.

Input
Four integer numbers representing the start and end time of the game.

Output
Print the duration of the game in hours and minutes, in this format: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” . Which means: the game lasted XXX hour(s) and YYY minutes.
"""

time = input().split(' ')

A, B, C, D = time

h1 = int(A)
m1 = int(B)
h2 = int(C)
m2 = int(D)

hour1 = (h1 * 60) + m1
hour2 = (h2 * 60) + m2
hour24 = 24 * 60

if hour2 > hour1:
    totaltime = hour2 - hour1
    h = int(totaltime / 60)
    m = totaltime % 60
    print('O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)'.format(h=h, m=m))
else:
    totaltime1 = hour24 - hour1
    totaltime2 = 0 + hour2
    totaltime = totaltime1 + totaltime2
    h = int(totaltime / 60)
    m = totaltime % 60
    print('O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)'.format(h=h, m=m))