print("Give me a number and I will tell you if it is an armstrong number or not.")
x=int(input())
digits_in_number_list=[]
j_power_digits_in_number_list=[]
sum_of_j_power_digits_in_number_list=[]
i=x
j=0
import pdb
pdb.set_trace()
while i>1:
    j=j+1
    i=i/10
print(j)
for m in range(j):
    digits_in_number_list.append(x%(pow(10, m)))
print(digits_in_number_list)
for n in range(len(digits_in_number_list)):
    j_power_digits_in_number_list.append(pow(digits_in_number_list[n], j))
for a in range(len(digits_in_number_list)):
    if len(sum_of_j_power_digits_in_number_list)==0:
        sum_of_j_power_digits_in_number_list.append(digits_in_number_list[a])
    else:
        sum_of_j_power_digits_in_number_list.append(sum_of_j_power_digits_in_number_list[len(sum_of_j_power_digits_in_number_list)-1]+digits_in_number_list[a])
print(len(sum_of_j_power_digits_in_number_list))
if sum_of_j_power_digits_in_number_list[len(sum_of_j_power_digits_in_number_list)-1]==x:
    print(x, "is an armstrong number.")
else:
    print(x, "is not an armstrong number.")
