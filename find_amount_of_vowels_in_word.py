print("Give me a word and I will tell you how many vowels it has and wiich ones they are.")
i_list=[]
a=input()
j=0
for i in range(len(a)):
    if (a[i]=='a') or (a[i]=='e') or (a[i]=='i') or (a[i]=='o') or (a[i]=='u'):
        i_list.append(a[i])
        j=j+1
if j==0:
    print("There are no vowels in", a, ".")
elif j==1:
    print("There is 1 vowel in", a, "and it is", end=" ")
else:
    print("There are", j, "vowels in", a, ". They are", end=" ")

for i in range(len(i_list)):
    if j==1:
        print(i_list[i], ".")
    elif i==(len(i_list)-1):
        print("and", i_list[i], ".")
    else:
        print(i_list[i], ",", end=" ")
