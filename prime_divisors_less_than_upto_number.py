from math import sqrt
print("Give me two numbers and I will tell you the numbers smaller than the first number, with prime divisors upto the second number. First, give me the first number.")
a=int(input())
print("Now, give me the second number.")
b=int(input())
print("Do you want to check the number or get the numbers up to it?(Please say 'check' or 'get to'.)")
c=input()
prime_list=[2]
for d in range(3, b+1):
    e=0
    f=0
    while prime_list[e]<=sqrt(d):
        if d%prime_list[e]==0:
            f=1
            break
        e=e+1
    if f==0:
        prime_list.append(d)
d=True
while d:
    if c=="check":
        d=False
        e=a
        f=0
        while f<len(prime_list):
            if e%prime_list[f]==0:
                e=e//prime_list[f]
            else:
                f=f+1
        if e==1:
            print(a, "follows these rules.")
        else:
            print(a, "does not follow these rules.")
    elif c=="get to":
        d=False
        e=0
        f=0
        for g in range(1, a+1):
            h=g
            i=0
            while i<len(prime_list):
                if h%prime_list[i]==0:
                    h=h//prime_list[i]
                else:
                    i=i+1
            if h==1:
                if e==0:
                    e=1
                    print("The such numbers are written below.")
                print(g)
                f=f+1
        if e==0:
            print("There are no such numbers.")
        else:
            print("So, there are", f, "such numbers.")
    else:
        print("Please say 'check' or 'get to'.")
        c=input()
