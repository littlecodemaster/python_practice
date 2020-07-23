import sys
print("Give me a number and I will tell you if it is a happy number or not.")
a=int(input())
b=a
past_members_list=[]
digits_list=[]
squares_of_digits_list=[]
while b!=1:
    past_members_list.append(b)
    #if len(past_members_list)==2:
    #    import pdb
    #    pdb.set_trace()
    for c in range(len(past_members_list)-1):
        if past_members_list[c]==past_members_list[len(past_members_list)-1]:
            print("This number is not a happy number. The route to repeating pattern is written below.")
            for d in range(c):
                print(past_members_list[d])
            print("The repeating pattern is written below.")
            for d in range(c, len(past_members_list)-1):
                print(past_members_list[d])
            sys.exit(0)
    c=b
    while c>0:
        digits_list.append(c%10)
        c=c//10
    for c in range(len(digits_list)):
        if c==0:
            squares_of_digits_list.append((digits_list[0])**2)
        else:
            squares_of_digits_list.append(squares_of_digits_list[c-1]+(digits_list[c])**2)
    b=squares_of_digits_list[len(squares_of_digits_list)-1]
    digits_list.clear()
    squares_of_digits_list.clear()
print(a, "is a happy number. It's route to 1 is written below.")
for a in range(len(past_members_list)):
    print(past_members_list[a])
print("1")
