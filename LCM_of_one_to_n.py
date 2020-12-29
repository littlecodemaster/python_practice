print("Give me a number and I will tell you the LCM of 1 to that number.")
a=int(input())
b=1
for c in range(1, a+1):
    d=b
    while b%c!=0:
        b=b+d
print("The LCM of 1 to", a, "is", b, end="")
print(".")
