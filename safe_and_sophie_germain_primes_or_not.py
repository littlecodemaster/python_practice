#!/usr/bin/python3
print ("Give me a number and I will tell you if it is prime or composite and if itx2+1 is prime or composite.")
n=float(input())
if n%1==0:
    j=0
    i=2
    if n>1:
        while i*i<=n:
            if n%i==0:
                if i==n/i:
                    print ("It is composite. It is divisible by", i, ".") 
                else:
                    print ("It is composite. It is divisible by", i, "and", n/i, ".")
                j=1
                break
            else:
                i=i+1
    else:
        j=1
        print("It is composite.")
    if j==0:
        print ("It is prime.")
    d=2*n+1
    j=0
    i=2
    if d>1:
        while i*i<=d:
            if d%i==0:
                if i==d/i:
                    print ("Itx2+1 is composite. It is divisible by", i, ".")
                else:
                    print ("Itx2+1 is composite. It is divisible by", i, "and", d/i, ".")
                j=1
                break
            else:
                i=i+1
    else:
        j=1
        print ("Itx2+1 is composite.")
    if j==0:
        print ("Itx2+1 is prime.")
else:
    print ("You can't divide", n, "into prime or composite because", n, "is a fraction.")
