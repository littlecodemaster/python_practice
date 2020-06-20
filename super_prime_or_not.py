print("Give me a number and I will tell you if it is super prime or not.")
number=int(input())
prime_list=[2]
i=3
while i<=number:
    j=0
    x=0
    while j<len(prime_list) and (prime_list[j])*(prime_list[j])<=i:
            if i%prime_list[j]==0:
                x=1
                break
            j=j+1
    if x==0:
        prime_list.append(i)
    i=i+1
if prime_list[len(prime_list)-1]==number:
    p=0
    d=0
    while prime_list[d]<=len(prime_list):
        if len(prime_list)==prime_list[d]:
            print(number, "is a super prime.")
            p=1
            break
        d=d+1
    if p==0:
        print(number, "is a prime, but not a super prime.")
else:
    print(number, "is not even a prime, let alone a super prime.")
