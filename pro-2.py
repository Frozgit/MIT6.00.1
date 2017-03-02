#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 18:59:50 2017

@author: il
"""
def closest_power (base, num):
    power=1
    while base**power<=num:
        power+=1
    if base**power>num:
        if abs(base**power-num)>=abs(base**(power-1)-num):
            power-=1
    return power
print(closest_power (7, 196.0))