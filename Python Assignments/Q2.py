# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 08:25:47 2015

@author: gerhard
"""

alphabet = list('abcdefghijklmnopqrstuvwxyz')
inputstring = raw_input('please enter a sentence to see if it contains all the letters in the alphabet ')

for letter in inputstring:
        if letter in alphabet:
            alphabet.remove(letter)
            
if alphabet == []:
    print 'they\'re all there!'