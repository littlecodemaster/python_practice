from math import sqrt
print("Give me a number and I will tell you how many divisors it's factorial has.")
a=int(input())
prime_list=[2]
powers_of_prime_list=[]
amount_of_repeatings=[]
multiplication_of_amount_of_repeatings=[]
for b in range(3, a+1):
    c=0
    d=0
    while prime_list[c]<=sqrt(b):
        if b%prime_list[c]==0:
            d=1
            break
        c=c+1
    if d==0:
        prime_list.append(b)
for b in range(len(prime_list)):
    c=b
    d=0
    while prime_list[c]**d<=a:
        d=d+1
    powers_of_prime_list.append(d)
for b in range(len(prime_list)):
    c=1
    for d in range(1, powers_of_prime_list[b]):
        c=c+(a//((prime_list[b])**d))
    amount_of_repeatings.append(c)
for b in range(len(amount_of_repeatings)):
    if b==0:
        multiplication_of_amount_of_repeatings.append(amount_of_repeatings[0])
    else:
        multiplication_of_amount_of_repeatings.append((amount_of_repeatings[b])*(multiplication_of_amount_of_repeatings[b-1]))
print("The amount of divisors of", a, "factorial is", multiplication_of_amount_of_repeatings[len(multiplication_of_amount_of_repeatings)-1], end="")
print(".")
