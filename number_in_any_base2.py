print("Give me x and y and I will tell you x in base y. First, give me x.")
x=int(input())
print("Now, give me y.")
y=int(input())
numbers_list=[]
print(x, "in base", y, "is", end=" ")
while x>0:
    numbers_list.append(x%y)
    x=x//y
for i in range(len(numbers_list)):
    print(numbers_list[len(numbers_list)-i-1], end="")
    if i<len(numbers_list)-1:
        print(",", end=" ")
    else:
        print(".")
