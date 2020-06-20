print("Tell me if you want the nth value or check your number.")
a=input()
fibonacci_list=[1, 1]
correct_format=False
while not correct_format:
    if a=="Check my number.":
        print("Then give me a number and I will tell you if it is a fibonacci number or not.")
        b=int(input())
        while fibonacci_list[len(fibonacci_list)-1]<b:
            fibonacci_list.append((fibonacci_list[len(fibonacci_list)-2])+(fibonacci_list[len(fibonacci_list)-1]))
        if (fibonacci_list[len(fibonacci_list)-1])==b:
            print(b, "is a fibonacci number.")
        else:
            print(b, "is not a fibonacci number.")
        correct_format=True
    elif a=="Nth value.":
        print("Then give me the n so that I will tell you the nth fibonacci number.")
        b=int(input())
        if b==1:
            print("1 is the 1st fibonacci number.")
        elif b==2:
            print("1 is the 2nd fibonacci number.")
        else:
            for i in range(b-2):
                fibonacci_list.append((fibonacci_list[len(fibonacci_list)-2])+(fibonacci_list[len(fibonacci_list)-1]))
            if b%10==1:
                print((fibonacci_list[len(fibonacci_list)-1]), "is the", b, "st fibonacci number.")
            elif b%10==2:
                print((fibonacci_list[len(fibonacci_list)-1]), "is the", b, "nd fibonacci number.")
            elif b%10==3:
                print((fibonacci_list[len(fibonacci_list)-1]), "is the", b, "rd fibonacci number.")
            else:
                print((fibonacci_list[len(fibonacci_list)-1]), "is the", b, "th fibonacci number.")
        correct_format=True
    else:
        print("Please say 'Nth value.' or 'Check my number.'")
        a=input()
