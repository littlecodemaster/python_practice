import copy
print("Give me a string and I will tell you what patterns repeat in it.")
a=input()
print("The repeating patterns are", end="")
possibilities_of_repeatation=[]
making_possibilities_of_repeatation=[]
actual=[]
letters=[]
for i in range(len(a)):
    letters.append([a[i]])
for i in range(len(a)):
    making_possibilities_of_repeatation.append(a[i])
    making_possibilities_of_repeatation2=copy.deepcopy(making_possibilities_of_repeatation)
    possibilities_of_repeatation.append(making_possibilities_of_repeatation2)
for i in range(len(a)):
    b=0
    for j in range(len(a)-i):
        k=j
        while len(possibilities_of_repeatation[i])<=k:
            k=k-(len(possibilities_of_repeatation))
        print("")
        print(possibilities_of_repeatation[i][k])
        print(possibilities_of_repeatation[i+j][len(possibilities_of_repeatation[i+j])-1])
        if not possibilities_of_repeatation[i][k]==possibilities_of_repeatation[i+j][len(possibilities_of_repeatation[i+j])-1]:
            b=1
    if b==0:
        actual.append(possibilities_of_repeatation[i])
for i in range(len(actual)):
    print(",", actual[i], end="")
print(".")
