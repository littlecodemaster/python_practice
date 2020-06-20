print("Do you want to find if a number is possible or not in the grid in grid puzzle?")
j=input()
if j=="yes":
    print("First, give me the first side of the grid.")
    i=int(input())
    print("Now, give me the second side of the grid.")
    j=int(input())
    print("Last, give me the number that you want to fit.")
    k=int(input())
    w=0
    for x in range(1, (i+1)):
        if k%x==0 and (k/x)<=j:
            print(x, "and", k/x, "can fit in", i, "and", j, ".")
            w=1
    if w==0:
        print("It is impossible to do it in this combination.")
else:
    print("Ok. See you later. Bye.")
