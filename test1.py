#!/usr/bin/python3

n=6
for i in range (n):
    if (i%2==1) and (i%3==1):
        print(i)
    if (i%2==1) and (i%3==2):
        print(i*i)
    else:
        print("What is your name?")
        name=input()
        print("Hi,", name)

