print("Give me a word and then give me a such part and I will tell you how many times it occurs in the word. First, give me the word.")
a=input()
print("Now, give me the part.")
b=input()
c=len(b)
word_groups_list=[]
for i in range((len(a)-c)+1):
     word_groups_list.append(a[i:(i+c)])
j=0
for k in range(len(word_groups_list)):
    if word_groups_list[k]==b:
        j=j+1
print("There are", j, b, "'s in", a, ".")
