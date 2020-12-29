print("Give me a number and I will tell you n such that n#=x(x+1) for integers n and x.")
from math import sqrt
a=int(input())
prime_list=[2]
prime_multiplication_list=[]
print("The such numbers are written below.")
for b in range(3, a+1):
    c=0
    d=0
    while prime_list[c]<=sqrt(b):
        if b%(prime_list[c])==0:
            d=1
            break
        c=c+1
    if d==0:
        prime_list.append(b)
for b in range(len(prime_list)):
    if b==0:
        prime_multiplication_list.append(2)
    else:
        prime_multiplication_list.append((prime_multiplication_list[b-1])*(prime_list[b]))
for b in range(len(prime_multiplication_list)):
    if (int(sqrt(prime_multiplication_list[b])))*(int(sqrt(prime_multiplication_list[b]))+1)==prime_multiplication_list[b]:
        print(prime_list[b])
