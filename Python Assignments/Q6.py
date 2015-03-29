# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 09:01:06 2015

@author: gerhard
"""

nuc = ['A', 'C', 'G', 'T', 'a', 'c', 'g', 't']

stringTheory = raw_input('enter a DNA sequence: ')

count = 0

for letter in stringTheory:
    if letter not in nuc:
        count+=1

print count