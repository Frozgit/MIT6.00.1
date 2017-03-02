#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 20:51:11 2017

@author: il
"""


x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while (guess**2-x)<epsilon:
    guess=x/2
    if (x-guess**2)>0:
        guess=x/2
    else:
        guess=x-guess**2
print (guess)
        