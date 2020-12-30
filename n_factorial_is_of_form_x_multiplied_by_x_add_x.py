from math import sqrt
print("Give me a number 'a' and I will tell you all the numbers less than 'a' who's factorial is of the form x*(x+1).")
a=int(input())
print("The such numbers are written below.")
factorial_list=[]
for b in range(1, a+1):
    if b==1:
        factorial_list.append(1)
    else:
        factorial_list.append((factorial_list[len(factorial_list)-1])*b)
for b in range(len(factorial_list)):
    if (int(sqrt(factorial_list[b])))*(int(sqrt(factorial_list[b]))+1)==factorial_list[b]:
        print(b+1)
