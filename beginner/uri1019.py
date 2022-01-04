# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 03:41:00 2021

@author: camil
"""

timeInSeconds = int(input())

hours = timeInSeconds // 3600
timeleft = timeInSeconds - hours*3600
minutes = timeleft // 60
seconds = timeleft - minutes*60

print('{}:{}:{}'.format(hours, minutes, seconds))