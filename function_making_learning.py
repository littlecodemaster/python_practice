def addition(x, y):
    print(x, "+", y, "=", x+y)
def subtraction(x, y):
    l_list=[x, y]
    l_list.sort()
    print(l_list[1], "-", l_list[0], "=", (l_list[1])-(l_list[0]))
def multiplication(x, y):
    print(x, "x", y, "=", x*y)
def division(x, y):
    l_list=[x, y]
    l_list.sort()
    if (l_list[1])%(l_list[0])==0:
        print(l_list[1], "by", l_list[0], "=", (l_list[1])/(l_list[0]))
def mathematics(x, y):
    addition(x, y)
    subtraction(x, y)
    multiplication(x, y)
    division(x, y)

x=3
y=9
mathematics(x, y)
aaaa=4
aaa=8
mathematics(aaa, aaaa)
