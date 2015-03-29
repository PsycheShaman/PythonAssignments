# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 08:35:27 2015

@author: gerhard
"""

inputThing = raw_input('please enter a word to see whether it is a palindrome: ')

list1 = []

for let in inputThing:
    list1.append(inputThing)

length = len(list1)
i = 0
j = length-1
k = 0
if length%2 == 0:
    print 'it\'s not a palindrome!'
else:
    while i <= length/2:
        i+=1
        while j >= length/2:
            j-=1
            if list1[i] == list1[j]:
                k+=1
                
if k == length/2 +1:
    print 'palindrome'