from math import sqrt
print("Give me a number 'a' and I will tell you the first 'k' such that 'k'*2^'n'+1 is prime for all 'n'<='a'.")
prime_list=[2]
a=int(input())
print("The numbers are written below in order.")
for b in range(1, a+1):
    k=1
    prime=False
    while not prime:
        for c in range(3, int(sqrt(k*(2**b))+1)+1):
            d=0
            e=0
            while prime_list[d]<=sqrt(c):
                if c%prime_list[d]==0:
                    e=1
                    break
                d=d+1
            if e==0:
                prime_list.append(c)
        c=0
        for d in range(len(prime_list)):
            if (k*(2**b)+1)%prime_list[d]==0:
                c=1
                break
        if c==0:
            print("for", b, "it is", k, end="")
            print(".")
            prime=True
        prime_list.clear()
        prime_list.append(2)
        k=k+1
