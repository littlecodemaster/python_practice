print("Give me x and y and I will tell you x in base y. First, give me x.")
x=int(input())
print("Now, give me y.")
y=int(input())
m=y
n=x
c=1
while m<=x:
    m=m*y
    c=c+1
c=c-1
print(x, "in base", y, "is", end=" ")
for i in range(c+1):
    d=0
    while n>=0:
        n=n-(y**(c-i))
        d=d+1
    d=d-1
    n=n+(y**(c-i))
    print(d, end="")
    if i==c:
        print(".")
    else:
        print(",", end=" ")
