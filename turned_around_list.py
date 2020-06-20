print("Give me a list and I will print it backwards.")
number_list=input()
print("[", end="")
for i in range(len(number_list)):
    if (len(number_list)-1)==i:
        print((number_list[(len(number_list))-i-1]), end="")
    else:
        print((number_list[(len(number_list))-i-1]), end=" ")
print("]")
