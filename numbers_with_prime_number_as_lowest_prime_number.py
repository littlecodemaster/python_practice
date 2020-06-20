print("Give me a prime number and another number and I will tell you all the numbers up to the other number in which the lowest prime divisor of that number is the prime number that you give me. First, give me the prime number.")
lowest_prime_number=int(input())
print("Now, give me the other number.")
end_number=int(input())
valid=False
q=0
while not valid:
    prime_list=[2]
    i=3
    while i<=lowest_prime_number:
        j=0
        x=0
        while j<len(prime_list) and (prime_list[j])*(prime_list[j])<=i:
                if i%prime_list[j]==0:
                    x=1
                    break
                else:
                    j=j+1
        if x==0:
            prime_list.append(i)
        i=i+1
    if (prime_list[len(prime_list)-1])==lowest_prime_number:
        valid=True
        m=0
        x=0
        for k in range(1, ((end_number//lowest_prime_number)+1)):
            y=0
            for l in range((len(prime_list))-1):
                if k%(prime_list[l])==0:
                    y=1
                    break
                l=l+1
            if y==0:
                if m==0:
                    print("The such numbers are written below.")
                m=1
                x=1
                print(lowest_prime_number*k)
                q=q+1
        if x==0:
            print("There are no such numbers.")
        else:
            print("So, there are", q, "such numbers.")
    else:
        print("The number which was supposed to be a prime number is not a prime number. Please try again.")
        lowest_prime_number=int(input())
        prime_list.clear()
