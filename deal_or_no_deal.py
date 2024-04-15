from random import shuffle
from sys import exit
the_money=[0.01, 0.05, 1, 5, 25, 100, 200, 500, 1000, 2000, 2500, 5000, 7500, 10000, 12500, 20000, 25000, 37500, 50000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
duplicate_the_money=[0.01, 0.05, 1, 5, 25, 100, 200, 500, 1000, 2000, 2500, 5000, 7500, 10000, 12500, 20000, 25000, 37500, 50000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
still_valid_numbers_to_take=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
shuffle(the_money)
the_money_to_duplicate_the_money={}
for i in range(26):
    j=0
    while duplicate_the_money[j]!=the_money[i]:
        j=j+1
    the_money_to_duplicate_the_money[i]=j
print("Welcome to deal or no deal!!! In this game, there are cases with money in them. You will first pick one case for yourself without opening it, and then you will pick 6 of the remaining cases and open them, one by one. The opening of the cases tells you which amounts of money you don't have. The cases have $0.01, $0.05, $1, $5, $25, $100, $200, $500, $1000, $2000, $2500, $5000, $7500, $10000, $12500, $20000, $25000, $37500, $50000, $100000, $200000, $300000, $400000, $500000, $750000, and 1 million dollars!!! Then you will get an offer. If you accept it, you get that much money and your box is revealed. If you decline it, you will pick a couple more cases (not 6 every time). If you keep declining it, then you will get the money in your case. To accept it, say deal. To decline it, say no deal. The cases are named by the numbers from 1 to 26. First, tell me the case you are picking.")
picked_case=int(input())
still_valid_numbers_to_take[picked_case-1]=0
#Now it is time for the 6, 5, 4, 3, 2 cases that come before an offer.
for i in range(1, 6):
    i2=7-i
    print("You are now going to pick", i2, "cases.")
    for j in range(i2):
        if not j==0:
            print("Next case!")
        print("The numbers that you can pick are", end="")
        for k in range(26):
            if not still_valid_numbers_to_take[k]==0:
                print(",", still_valid_numbers_to_take[k], end="")
        print(".")
        print("The cases still remaining are dollars", end="")
        for k in range(26):
            if not duplicate_the_money[k]==0:
                print(",", duplicate_the_money[k], end="")
        print(".")
        opened_case=int(input())
        while True:
            if opened_case in still_valid_numbers_to_take and not opened_case==0:
                break
            print("Please give a valid case.")
            opened_case=int(input())
        still_valid_numbers_to_take[opened_case-1]=0
        print("You opened the case with", the_money[opened_case-1], "dollars.")
        duplicate_the_money[the_money_to_duplicate_the_money.get(opened_case-1)]=0
        the_money[opened_case-1]=0
        number_nonzero_elements=0
        sum_elements=0
        for k in range(26):
            sum_elements=sum_elements+the_money[k]
            if not the_money[k]==0:
                number_nonzero_elements=number_nonzero_elements+1
        avg_elements=sum_elements//number_nonzero_elements*8//9
        if not avg_elements<1:
            avg_elements=int(avg_elements)
    print("Your offer is... drumroll please...", avg_elements, "dollars! Deal or no deal? Please give your answer in all lowercase.")
    deal_or_no_deal=input()
    while True:
        if deal_or_no_deal=='deal':
            print("Ok, you got your", avg_elements, "dollars. Your case contained", the_money[picked_case-1], "dollars.", end=" ")
            if avg_elements>the_money[picked_case-1]:
                print("That means you made a good decision!")
            elif avg_elements<the_money[picked_case-1]:
                print("Oops, you should have kept on playing.")
            else:
                print("OMG!!! Such a rare case!!! It didn't matter!!!")
            exit(0)
        elif deal_or_no_deal=='no deal':
            print("Ok, let's keep on playing!")
            break
        else:
            print("Sorry, I didn't understand that. Could you please repeat that?")
            deal_or_no_deal=input()
#Now it is time for the singular 2 cases that come before an offer.
print("You are now going to pick 2 cases.")
for j in range(2):
    if not j==0:
        print("Next case!")
    print("The numbers that you can pick are", end="")
    for k in range(26):
        if not still_valid_numbers_to_take[k]==0:
            print(",", still_valid_numbers_to_take[k], end="")
    print(".")
    print("The cases still remaining are dollars", end="")
    for k in range(26):
        if not duplicate_the_money[k]==0:
            print(",", duplicate_the_money[k], end="")
    print(".")
    opened_case=int(input())
    while True:
        if opened_case in still_valid_numbers_to_take and not opened_case==0:
            break
        print("Please give a valid case.")
        opened_case=int(input())
    still_valid_numbers_to_take[opened_case-1]=0
    print("You opened the case with", the_money[opened_case-1], "dollars.")
    duplicate_the_money[the_money_to_duplicate_the_money.get(opened_case-1)]=0
    the_money[opened_case-1]=0
    number_nonzero_elements=0
    sum_elements=0
    for k in range(26):
        sum_elements=sum_elements+the_money[k]
        if not the_money[k]==0:
            number_nonzero_elements=number_nonzero_elements+1
    avg_elements=sum_elements//number_nonzero_elements*8//9
    if not avg_elements<1:
        avg_elements=int(avg_elements)
print("Your offer is... drumroll please...", avg_elements, "dollars! Deal or no deal? Please give your answer in all lowercase.")
deal_or_no_deal=input()
while True:
    if deal_or_no_deal=='deal':
        print("Ok, you got your", avg_elements, "dollars. Your case contained", the_money[picked_case-1], "dollars.", end=" ")
        if avg_elements>the_money[picked_case-1]:
            print("That means you made a good decision!")
        elif avg_elements<the_money[picked_case-1]:
            print("Oops, you should have kept on playing.")
        else:
            print("OMG!!! Such a rare case!!! It didn't matter!!!")
        exit(0)
    elif deal_or_no_deal=='no deal':
        print("Ok, let's keep on playing!")
        break
    else:
        print("Sorry, I didn't understand that. Could you please repeat that?")
        deal_or_no_deal=input()
#Now it is time for the 3 times you ask for 1 case that comes before an offer.
for i in range(2):
    print("You are now going to pick 1 case.")
    print("The numbers that you can pick are", end="")
    for k in range(26):
        if not still_valid_numbers_to_take[k]==0:
            print(",", still_valid_numbers_to_take[k], end="")
    print(".")
    print("The cases still remaining are dollars", end="")
    for k in range(26):
        if not duplicate_the_money[k]==0:
            print(",", duplicate_the_money[k], end="")
    print(".")
    opened_case=int(input())
    while True:
        if opened_case in still_valid_numbers_to_take and not opened_case==0:
            break
        print("Please give a valid case.")
        opened_case=int(input())
    still_valid_numbers_to_take[opened_case-1]=0
    print("You opened the case with", the_money[opened_case-1], "dollars.")
    duplicate_the_money[the_money_to_duplicate_the_money.get(opened_case-1)]=0
    the_money[opened_case-1]=0
    number_nonzero_elements=0
    sum_elements=0
    for k in range(26):
        sum_elements=sum_elements+the_money[k]
        if not the_money[k]==0:
            number_nonzero_elements=number_nonzero_elements+1
    avg_elements=sum_elements//number_nonzero_elements*8//9
    if not avg_elements<1:
        avg_elements=int(avg_elements)
    print("Your offer is... drumroll please...", avg_elements, "dollars! Deal or no deal? Please give your answer in all lowercase.")
    deal_or_no_deal=input()
    while True:
        if deal_or_no_deal=='deal':
            print("Ok, you got your", avg_elements, "dollars. Your case contained", the_money[picked_case-1], "dollars.", end=" ")
            if avg_elements>the_money[picked_case-1]:
                print("That means you made a good decision!")
            elif avg_elements<the_money[picked_case-1]:
                print("Oops, you should have kept on playing.")
            else:
                print("OMG!!! Such a rare case!!! It didn't matter!!!")
            exit(0)
        elif deal_or_no_deal=='no deal':
            print("Ok, let's keep on playing!")
            break
        else:
            print("Sorry, I didn't understand that. Could you please repeat that?")
            deal_or_no_deal=input()
print("You got... drumroll please...", the_money[picked_case-1], "dollars! (Because there is only one choice for the last one, I didn't ask you for that one.)")
