# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 03:41:00 2021

@author: camila

Time Conversion

Read an integer value, which is the duration in seconds of a certain event in a factory, and inform it expressed in hours:minutes:seconds.

Input
The input file contains an integer N.

Output
Print the read time in the input file (seconds) converted in hours:minutes:seconds like the following example.
"""

timeInSeconds = int(input())

hours = timeInSeconds // 3600
timeleft = timeInSeconds - hours*3600
minutes = timeleft // 60
seconds = timeleft - minutes*60

print('{}:{}:{}'.format(hours, minutes, seconds))