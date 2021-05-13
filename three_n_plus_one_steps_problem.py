# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 01:39:15 2021

@author: mvjoshi
"""

print("Give me a number and I will tell you how many steps it's 3n+1 took, then how many steps the answer of the first's 3n+1 took, et cetera, until it reaches 0.")
beginning_number=int(input())
print("")
print(beginning_number)
current_place=beginning_number
current_place2=beginning_number
chain=0
while not current_place==0:
    current_number=current_place
    current_number2=current_place2
    steps=0
    while not current_number==1:
        if current_number%2==1:
            current_number=3*current_number+1
        else:
            current_number=current_number//2
        steps=steps+1
    print(steps)
    current_place=steps
    chain=chain+1
print("So, there were", chain, "steps in the process of", beginning_number, ".")