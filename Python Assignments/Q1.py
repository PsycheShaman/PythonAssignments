# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 08:19:41 2015

@author: gerhard
"""

song1 = 'bottles of beer on the wall '
song2 = 'bottles of beer '
song3 = 'take one down pass it around '
i = 99

while i>= 0:
    print str(i) + ' ' + song1 + str(i) + ' ' + song2 + song3 + str(i) + ' ' + song1
    i-=1