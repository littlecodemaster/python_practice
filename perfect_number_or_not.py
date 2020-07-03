from math import sqrt
print("Give me a number and I will tell you if it is a perfect number or not.")
a=int(input())
b=a
c=1
prime_list=[2]
while b%2==0:
    b=b//2
    c=2*c
if b==2*c-1:
    for b in range(3, b+1):
        d=0
        e=0
        while prime_list[d]<sqrt(b):
            if b%prime_list[d]==0:
                e=1
                break
            d=d+1
        if e==0:
            prime_list.append(b)
    if prime_list[len(prime_list)-1]==b:
        print("This is a perfect number in which the mersenne prime is", b, end="")
        print(".")
    else:
        print("This is not a perfect number because the mersenne number is not prime.")
else:
    print("This is not a perfect number. It is either not made of a mersenne number or has the wrong power of 2.")
