# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 22:33:13 2022

@author: camila

Event Time

Peter is organizing an event in his University. The event will be in April month, beginning and finishing within April month. The problem is: Peter wants to calculate the event duration in seconds, knowing obviously the begin and the end time of the event.

You know that the event can take from few seconds to some days, so, you must help Peter to compute the total time corresponding to duration of the event.

Input
The first line of the input contains information about the beginning day of the event in the format: “Dia xx”. The next line contains the start time of the event in the format presented in the sample input. Follow 2 input lines with same format, corresponding to the end of the event.

Output
Your program must print the following output, one information by line, considering that if any information is null for example, the number 0 must be printed in place of W, X, Y or Z:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Consider that the event of the test case have the minimum duration of one minute. “dia” means day, “hora” means hour, “minuto” means minute and “Segundo” means second in Portuguese.
"""
day1 = input().split(' ')
time1 = input().split(':')
day2 = input().split(' ')
time2 = input().split(':')

A, B = day1
C, D, E = time1
F, G = day2
H, I, J = time2

b = int(B)
c = int(C)
d = int(D)
e = int(E)
g = int(G)
h = int(H)
i = int(I)
j = int(J)

inicialday = (((b * 24) * 60) * 60)
inicialhour = ((c * 60) * 60)
inicialminute = (d * 60)
inicialtime = inicialday + inicialhour + inicialminute + e
finalday = (((g * 24) * 60) * 60)
finalhour = ((h * 60) * 60)
finalminute = (i * 60)
finaltime = finalday + finalhour + finalminute + j

totaltime = finaltime - inicialtime

days = totaltime // 86400
v1 = totaltime % 86400
hours = v1 // 3600
v2 = v1 % 3600
minutes = v2 // 60
seconds = v2 % 60
print('{} dia(s)'.format(days))
print('{} hora(s)'.format(hours))
print('{} minuto(s)'.format(minutes))
print('{} segundo(s)'.format(seconds))

















