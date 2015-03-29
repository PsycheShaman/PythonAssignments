# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 09:08:09 2015

@author: gerhard
"""

inputnum = input('enter a number: ')

ranger = range(0,inputnum,1)

e = long(0.0)

for stuff in ranger:
    i=stuff
    listnum =[]
    
    while i > 0:
        listnum.append(i)
        i-=1
    
    multsum = 1.0
    
    for item in listnum:
        multsum *= item 

    formula = 1.0/multsum
    e+=formula
    
print e