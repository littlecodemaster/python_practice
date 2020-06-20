print("Tell me two numbers that x into one of them plus y into the other is the third number. First, give the first number.")
first_number=int(input())
print("Now the second number.")
second_number=int(input())
print("Now print the number that is the goal.")
goal_number=int(input())
i=0
x=0
while first_number*i<=goal_number:
    j=0
    while (second_number*j)<=(goal_number-first_number*i):
        if (second_number*j)==(goal_number-first_number*i):
            print(i, "x", first_number, "+", j, "x", second_number, "=", goal_number)
            x=1
            break
        j=j+1
    i=i+1
if x==0:
    print("There are no such pairs.")
