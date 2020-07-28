print("Give me a number and I will tell you if it is a woodall number or a cullen number or none.")
a=int(input())
b=0
c=0
while (b*(2**b))-2<a:
    #import pdb
    #pdb.set_trace()
    if ((b*(2**b))+1)==a:
        print(a, "is a cullen number when n is", b, end="")
        print(".")
        c=1
        break
    elif ((b*(2**b))-1)==a:
        print(a, "is a woodall number when n is", b, end="")
        print(".")
        c=1
        break
    b=b+1
if c==0:
    print("This is not a cullen number nor a woodall number.")
