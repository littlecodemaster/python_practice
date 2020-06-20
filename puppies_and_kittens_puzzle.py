print("Give me a number and I will tell you the puppies and kittens puzzle bad number groups up to it.")
upto_number=int(input())
tried_list=[]
used_list=[]
numbers_in_used_list=0
first_number=1
second_number=2
print(first_number, ",", second_number)
tried_list.append(first_number)
used_list.append(second_number)
numbers_in_used_list=numbers_in_used_list+1
for i in range(2, upto_number+1):
    first_number=first_number+1
    x=1
    j=0
    while (j<numbers_in_used_list) and (used_list[j] <= first_number):
        if used_list[j]==first_number:
            print(first_number, ",", tried_list[j])
            second_number=second_number+1
            x=0
        j=j+1
    if x==1:
        second_number=second_number+2
        print(first_number, ",", second_number)
        tried_list.append(first_number)
        used_list.append(second_number)
        numbers_in_used_list=numbers_in_used_list+1
