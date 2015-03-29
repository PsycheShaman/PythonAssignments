# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 08:51:34 2015

@author: gerhard
"""

inputnum = input('enter a number to see it\'s factorial: ')

i=inputnum
listnum =[]

while i > 0:
    listnum.append(i)
    i-=1

multsum = 1

for item in listnum:
    multsum *= item
    
print multsum