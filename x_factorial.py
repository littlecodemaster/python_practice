print("Give me any number and I will tell you it's factorial.")
x=int(input())
factorial_list=[2]
for i in range(3, (x+1)):
    factorial_list.append((factorial_list[len(factorial_list)-1])*i)
if x==0:
    print("The factorial of 0 is 0.")
if x==1:
    print("The factorial of 1 is 1.")
print("The factorial of", x, "is", factorial_list[len(factorial_list)-1], ".")
