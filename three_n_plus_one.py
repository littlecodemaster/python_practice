# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 02:13:28 2021

@author: mvjoshi
"""

print("Give me a number and I will tell you it's 3n+1 sequence, how many steps it took, how many high records there are, how many low records there are, and how many odd low records there are.")
input_number=int(input())
print(input_number, end=", ")
current_number=input_number
steps=0
small_numbers=1
small_number=current_number
large_numbers=1
large_number=current_number
if current_number%2==1:
    small_odd_numbers=1
    small_odd_number=current_number
else:
    small_odd_numbers=0
    small_odd_number=input_number+1
while not current_number==1:
    if current_number%2==1:
        current_number=3*current_number+1
        if current_number>large_number:
            large_number=current_number
            large_numbers=large_numbers+1
    else:
        current_number=current_number//2
        if current_number<small_odd_number:
            small_number=current_number
            small_numbers=small_numbers+1
            if current_number%2==1:
                small_odd_number=current_number
                small_odd_numbers=small_odd_numbers+1
    print(current_number, end="")
    print(",", end=" ")
    steps=steps+1
print("")
print("There are", large_numbers, "large numbers, the largest being", large_number, ",", small_numbers, "small numbers, and", small_odd_numbers, "small odd numbers.")
print("And, altogether, the 3n+1 for", input_number, "took", steps, "steps.")