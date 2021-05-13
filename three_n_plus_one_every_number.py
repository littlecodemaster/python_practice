# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 03:17:24 2021

@author: mvjoshi
"""

print("Give me two numbers and I will tell you if all the 3n+1's of the numbers between those numbers reach a smaller number. Smaller number first:")
small_number=int(input())
print("Now larger number please:")
large_number=int(input())
a=0
current_number=small_number
while not current_number%4==3:
    current_number=current_number+1
while current_number<large_number+1:
    current_place=current_number
    if current_place%2==1:
        current_place=3*current_place+1
    else:
        current_place=current_place//2
    while current_place>current_number:
        if current_place%2==1:
            current_place=3*current_place+1
        else:
            current_place=current_place//2
    if current_place==current_number:
        print(current_number, "has fallen into a repeating pattern. I will show it to you in a sec.")
        print(current_place)
        if current_place%2==1:
            current_place=3*current_place+1
            print(current_place)
        else:
            current_place=current_place//2
            print(current_place)
        while current_place>current_number:
            if current_place%2==1:
                current_place=3*current_place+1
                print(current_place)
            else:
                current_place=current_place//2
                print(current_place)
        a=1
    current_number=current_number+4
if a==0:
    print("I have not found any repeating patterns in these numbers.")
else:
    print("These are the only repeating patterns in these numbers.")