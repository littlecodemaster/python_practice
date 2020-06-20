import sys
print("Give me three numers l, m, and n and I will tell you the nth number that is m(mod l) in the fibonacci sequence. First, give me n.")
n=int(input())
print("Now, give me m.")
m=int(input())
print("Now, give me l.")
l=int(input())
correct_typed_fibonacci_number_list=[]
fibonacci_number_list=[1, 1]
if m==1:
    if n==1:
        print("The first such number is [1].")
        sys.exit(0)
    elif n==2:
        print("The first 2 such numbers are 1, 1.")
        sys.exit(0)
    else:
        correct_typed_fibonacci_number_list.append(1)
        correct_typed_fibonacci_number_list.append(1)
while (len(correct_typed_fibonacci_number_list))<n:
    fibonacci_number_list.append((fibonacci_number_list[len(fibonacci_number_list)-1])+(fibonacci_number_list[len(fibonacci_number_list)-2]))
    if (fibonacci_number_list[len(fibonacci_number_list)-1])%m==l:
        correct_typed_fibonacci_number_list.append(fibonacci_number_list[len(fibonacci_number_list)-1])
if n==0:
    print("There won't be any since you said the first 0.")
elif n==1:
    print("The first such number is", correct_typed_fibonacci_number_list[0])
else:
    print("The first", n, "such numbers are", end=" ")
for i in range(len(correct_typed_fibonacci_number_list)):
    if i==(len(correct_typed_fibonacci_number_list)-1):
        print("and", end=" ")
    print(correct_typed_fibonacci_number_list[i], end="")
    if i==(len(correct_typed_fibonacci_number_list)-1):
        print(".")
    else:
        print(",", end=" ")
print("They are in places", end=" ")
for i in range(len(correct_typed_fibonacci_number_list)):
    for j in range(len(fibonacci_number_list)):
        if correct_typed_fibonacci_number_list[i]==fibonacci_number_list[j]:
            if i==(len(correct_typed_fibonacci_number_list)-1):
                print("and", end=" ")
            print(j, end="")
            if i==(len(correct_typed_fibonacci_number_list)-1):
                print(".")
            else:
                print(",", end=" ")

