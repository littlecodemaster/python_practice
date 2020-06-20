print("Give me some numbers and I will tell you if they are in order or not.")
numbers_list=input()
print("Do you want them in increasing order, or decreasing order?(Say 'increasing order' or 'decreasing order'.)")
type_of_order=input()
valid=False
correct=False
while not valid:
    if type_of_order=="increasing order":
        valid=True
        while not correct:
            x=0
            for i in range(len(numbers_list)):
                #if not isnumeric(numbers_list[i]):
                if numbers_list[i].isnumeric()==False:
                    print("Please only give me numbers in the list that I am checking. Now give it to me again.")
                    numbers_list=input()
                    x=1
                    break
            if x==0:
                correct=True
        for i in range(len(numbers_list)-1):
            x=0
            if not i==0:
                if not (numbers_list[i])>(numbers_list[i-1]):
                    x=1
                    print("This is not true because", numbers_list[i-1], "is greater than", number_list[i], end="")
                    print(".")
        if x==0:
            print("This is true.")
    elif type_of_order=="decreasing order":
        valid=True
        while not correct:
            x=0
            for i in range(len(numbers_list)):
                if not isnumeric(numbers_list[i]):
                    print("Please only give me numbers in the list that I am checking. Now give it to me again.")
                    numbers_list=input()
                    x=1
                    break
            if x==0:
                correct=True
        for i in range(len(numbers_list)-1):
            x=0
            if not i==0:
                if not (numbers_list[i-1])>(numbers_list[i]):
                    x=1
                    print("This is not true because", numbers_list[i-1], "is less than", number_list[i], end="")
                    print(".")
        if x==0:
            print("This is true.")
    else:
        print("For 'do you want them in increasing order, or decreasing order', please say 'increasing order' or 'decreasing order'.")
        type_of_order=input()
