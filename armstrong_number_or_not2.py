print("Give me a number and I will tell you if it is an armstrong number or not.")
x=int(input())
digits_in_number_list=[]
j_power_digits_in_number_list=[]
sum_of_j_power_digits_in_number_list=[]
i=x
j=0
l=x
while i>1:
    j=j+1
    i=i/10
for k in range(j):
    digits_in_number_list.append(l%10)
    l=l//10
for n in range(len(digits_in_number_list)):
    j_power_digits_in_number_list.append(pow(digits_in_number_list[n], j))
for a in range(len(digits_in_number_list)):
    if len(sum_of_j_power_digits_in_number_list)==0:
        sum_of_j_power_digits_in_number_list.append(j_power_digits_in_number_list[a])
    else:
        sum_of_j_power_digits_in_number_list.append(sum_of_j_power_digits_in_number_list[len(sum_of_j_power_digits_in_number_list)-1]+j_power_digits_in_number_list[a])
if sum_of_j_power_digits_in_number_list[len(sum_of_j_power_digits_in_number_list)-1]==x:
    print(x, "is an armstrong number.")
else:
    print(x, "is not an armstrong number.")

