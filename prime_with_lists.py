#for i in range(number):
#    while (prime_list[-1])<(sqrt(number)):
#        for j in range(number_of_primes):
#from math import sqrt
print("Give me a number and I will tell you all the primes or composites up to it.")
number=int(input())
print("Do you want prime numbers or composite numbers?")
type_of_number=input()
prime_list=[2]
number_of_primes=1
i=3
if "prime"==type_of_number:
    print(prime_list[0])
    while i<=number:
        j=0
        x=0
        while j<number_of_primes and (prime_list[j])*(prime_list[j])<=i:
                if i%prime_list[j]==0:
                    x=1
                    break
                else:
                    j=j+1
        if x==0:
            print(i)
            prime_list.append(i)
            number_of_primes=number_of_primes+1
        i=i+1
if "composite"==type_of_number:
    while i<=number:
        j=0
        x=0
        while j<number_of_primes and (prime_list[j])*(prime_list[j]):
            if i%prime_list[j]==0:
                print(i)
                x=1
                break
            else:
                j=j+1
        if x==0:
            prime_list.append(i)
            number_of_primes=number_of_primes+1
        i=i+1
