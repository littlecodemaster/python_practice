number_list=[109, 109, -109, 109]
amount_of_numbers=len(number_list)
runnerup=0
winner=0
if number_list[0]<number_list[1]:
    winner=number_list[1]
    runnerup=number_list[0]
else:
    runnerup=number_list[1]
    winner=number_list[0]
for i in range(2,len(number_list)):
    if number_list[i]>winner:
        runnerup=winner
        winner=number_list[i]
    elif number_list[i]>runnerup:
        runnerup=number_list[i]
if winner==runnerup:
    print("The winner is tied with the runnerup because they both are", winner)
else:
    print("The winner is", winner, "and the runnerup is", runnerup)
