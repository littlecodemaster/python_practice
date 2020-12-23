from math import ceil
print("Give me a number and I will tell you how many times you would have to shuffle that many cards so that you return to the same combination.")
amt_cds=int(input())
repeatations=0
shuffled_list=[]
beginning_list=[]
for shuffled_list_filler in range(amt_cds):
    shuffled_list.append(shuffled_list_filler+1)
    beginning_list.append(shuffled_list_filler+1)
print(shuffled_list)
repeating_pattern=False
grouping=ceil(amt_cds/2)
while not repeating_pattern:
    group1_list=shuffled_list[0:grouping]
    group2_list=shuffled_list[grouping:amt_cds]
    shuffled_list.clear()
    while len(shuffled_list)<amt_cds:
        shuffled_list.append(group1_list[0])
        group1_list.remove(group1_list[0])
        if len(group2_list)>0:
            shuffled_list.append(group2_list[0])
            group2_list.remove(group2_list[0])
    print(shuffled_list)
    repeatations=repeatations+1
    if shuffled_list==beginning_list:
        repeating_pattern=True
print("So, there is a cycle of", repeatations, "permutations with", amt_cds, "cards for the card shuffling problem.")
