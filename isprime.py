#!/usr/bin/python3
n = 100
if not (n%2==0) or (n%3==0) or (n%5==0) or (n%7==0):
    print (str(n) + " is a composite number.")
else:
    print(str(n) + " is a prime number.")
