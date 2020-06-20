from math import sqrt
import sys
print("Give me a number and I will tell you if it is a leyland number or not.")
a=int(input())
b=0
for i in range(2, (int(sqrt(a))+1)):
    j=2
    while pow(j, i)+pow(i, j)<=a:
        if (pow(j, i))+(pow(i, j))==a:
            print(a, "is a leyland number in which x is", j, "and y is", i, ".")
            b=1
            sys.exit(0)
        j=j+1
if b==0:
    print(a, "is not a leyland number.")
