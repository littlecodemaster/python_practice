from math import sqrt
print("Give me a number and I will tell you the numbers up to it that are in the form x^y in which y is not 1.")
a=int(input())
print("Do you want the numbers as such or not as such?(Please say 'as such' or 'not as such'.)")
b=input()
such=[]
not_such=[]
for d in range(a+1):
    c=round(sqrt(d))
    e=0
    for f in range(1, round(sqrt(d))+1):
        impossible=True
        while impossible:
            if c**f<=d:
                impossible=False
            else:
                c=c-1
        if c**f==d:
            such.append(d)
            e=1
            break
    if e==0:
        not_such.append(d)
invalid=True
while invalid:
    if b=="as such":
        print("Those numbers are written below.")
        for g in range(len(such)):
            print(such[g])
        invalid=False
    elif b=="not as such":
        print("Those numbers are written below.")
        for g in range(1, len(not_such)):
            print(not_such[g])
        invalid=False
    else:
        print("Please say 'as such' or 'not as such'.")
