print("Give me a group of few numbers and I will tell you the sum of their nth power. First, give me the lower number.")
lower_number=int(input())
print("Now, give me the top number.")
higher_number=int(input())
print("Last, give me n.")
n=int(input())
nth_power_list=[]
sum_of_nth_power_list=[]
for i in range(lower_number, (higher_number+1)):
    if i==lower_number:
        if n%10==1:
            print("The sum of", n, end="")
            print("st power of the numbers", i, end="")
        elif n%10==2:
            print("The sum of", n, end="")
            print("nd power of the numbers", i, end="")
        elif n%10==3:
            print("The sum of", n, end="")
            print("rd power of the numbers", i, end="")
        else:
            print("The sum of", n, end="")
            print("th power of the numbers", i, end="")
        print(",", end=" ")
    elif i==higher_number:
        print(i, end=" ")
        print("or")
    else:
        print(i, end="")
        print(",", end=" ")
for i in range(lower_number, (higher_number+1)):
    if i==higher_number:
        print(i**n, end=" ")
        print("is")
    elif i==lower_number:
        print("The sum of the numbers", i**n, end="")
        print(",", end=" ")
    else:
        print(i**n, end="")
        print(",", end=" ")
    nth_power_list.append(i**n)
for i in range(len(nth_power_list)):
    if i==0:
        sum_of_nth_power_list.append(nth_power_list[0])
    else:
        sum_of_nth_power_list.append((sum_of_nth_power_list[i-1])+(nth_power_list[i]))
print(sum_of_nth_power_list[len(sum_of_nth_power_list)-1], end="")
print(".")
