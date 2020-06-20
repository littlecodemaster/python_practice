print("Give me a word and I will tell you how much of it is in increasing alphabetical order.")
a=input()
alphabets_list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabetical_parts_list=[]
biggest_alphabetical_group=[]
j_list=[]
past_list=[]
#valid=False
#while not valid:
#    if isalpha():
for i in range(len(a)):
    for j in range(26):
        if alphabets_list[j]==a[i]:
            if not len(past_list)==0:
                past_list.clear()
            past_list.append(j)
            if (len(j_list))==0 or past_list[0]<=j:
                j_list.append(a[i])
            else:
                alphabetical_parts_list.append(j_list)
                j_list.clear()
import pdb
pdb.set_trace()
if not (len(j_list))==0:
    alphabetical_parts_list.append(j_list)
for l in range(len(alphabetical_parts_list)):
    if l==0 or (len(biggest_alphabetical_group[len(biggest_alphabetical_group)-1]))<(len(alphabetical_parts_list[l])):
        biggest_alphabetical_group.append(alphabetical_parts_list[l])
b=biggest_alphabetical_group[len(biggest_alphabetical_group)-1]
print("The biggest part in alphabetical order in", a, "is", b, "which has", len(b), "letters.")
#        valid=True
#    else:
#        print("Please enter something with only letters or I will not understand where to put the numbers in the order.")
