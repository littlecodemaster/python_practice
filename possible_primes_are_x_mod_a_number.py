from math import sqrt
print("Give me a number and I will tell you all the possible mod that number that are possible to be prime.")
mod_number=int(input())
print("The such moded numbers are", end="")
l=mod_number
prime_list=[2]
divisors_list=[]
i=3
while i<=mod_number:
    j=0
    k=0
    while prime_list[j]<sqrt(i):
        if i%prime_list[j]==0:
            k=1
            break
        j=j+1
    if k==0:
        prime_list.append(i)
    i=i+1
j=0
while j<len(prime_list):
    if l%prime_list[j]==0:
        divisors_list.append(prime_list[j])
        l=l//prime_list[j]
    j=j+1
m=0
for i in range(mod_number):
    k=0
    for j in range(len(divisors_list)):
        if i%divisors_list[j]==0:
            k=1
            break
    if k==0:
        print(",", i, end="")
        m=m+1
print(". So there are", m, "such numbers mod", mod_number, end="")
print(".")
