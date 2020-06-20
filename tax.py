#!/usr/bin/python3
#if i<=9700:
#   print ("Your tax is", i*.1)
#elif i<=39475:
#    print ("Your tax is", 970+(i-9700)*.12)
#elif i<=84200:
#    print ("Your tax is", 4543+(i-39475)*.22)
#elif i<=160725:
#    print ("Your tax is", 14382.5+(i-84200)*.24)
#elif i<=204100:
#    print ("Your tax is", 32748.5+(i-160725)*.32)
#elif i<=510300:
#    print ("Your tax is", 46628.5+(i-204100)*.35)
#else:
#    print ("Your tax is", 153798.5+(i-510300)*.37)
print ("Give me your income and i'll tell you your tax.")
income=float(input())
tax_list=(.1, .12, .22, .24, .32, .35, .37)
income_list=(9700, 39475, 84200, 160725, 204100, 510300)
cutoff_list=(0, 0, 0, 0, 0, 0)
cutoff_list[0]=income_list[0]*tax_list[0]
for i in range(1,6):
    cutoff_list[i]=(income_list[i]-income_list[i-1])*tax_list[i]
