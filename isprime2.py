print ("Give me a number and I will tell you if it is prime or composite.")
n=int(input())
i=2
j=0
while i*i<=n:
    if n%i==0:
        print (n,"is a composite number and is divisible by", i, ".")
        j=1
        break
    i=i+1
if j==0:
    print(n, "is a prime number.")
