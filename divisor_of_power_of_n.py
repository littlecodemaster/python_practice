from math import sqrt
print("Give me two numbers 'a' and 'b' and I will tell you all the numbers up to 'a' that are not divisible by any number power 'b'. First, give me 'a'.")
a=int(input())
print("Now, give me 'b'.")
b=int(input())
print("The such numbers are written below.")
c=0
f=0
prime_list=[2]
while c**b<=a:
    c=c+1
for d in range(3, c):
    e=0
    f=0
    while prime_list[f]<sqrt(d):
        if d%prime_list[f]==0:
            e=1
            break
        f=f+1
    if e==0:
        prime_list.append(d)
for c in range(2, a):
    d=0
    e=0
    while (prime_list[e]**b)<=c:
        if c%(prime_list[e]**b)==0:
            d=1
            break
        if not (e+1)==len(prime_list):
            e=e+1
        else:
            break
    if d==0:
        f=f+1
        print(c)
print("So, there are", f, "such numbers.")
