# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 18:18:22 2019

@author: advait
"""
#NiceHexSpiral.py
import turtle
colors=['red', 'purple', 'blue','green']
t=turtle.Pen()
t.speed(0)

turtle.bgcolor('white')
for x in range(200):
    t.pencolor(colors[x%4])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)      
