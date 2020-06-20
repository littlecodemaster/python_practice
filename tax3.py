

#cutoff_list = [0, 0, 0, 0, 0, 0]

#print(cutoff_list[0])

def calc_income(income, tax_list,income_list):
    cutoff_list=[0]*len(income_list)
    cutoff_list[0]=tax_list[0]*income_list[0]
    for i in range (1,len(income_list)):
        cutoff_list[i]=cutoff_list[i-1]+(income_list[i]-income_list[i-1])*tax_list[i]
        print(cutoff_list[i])

    i=0
    while (i < len(income_list)):
        if  income < income_list[i]:
            break
        else:
            i=i+1

    if (i>0):
        tax = cutoff_list[i-1] + (income - income_list[i-1]) * tax_list[i]
        #print("printing tax")
        #print(tax)
    else:
        tax=income*tax_list[0]
        #print("printing tax")
        #print(tax)
    return(tax)

print ("Give me your income and i'll tell you your tax.")
myincome=float(input())
print("Tell me the tax year, either 2019 or 2020")
tax_yr = int(input())

if tax_yr==2019:
    mytax_list = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]
    myincome_list=[9700, 39475, 84200, 160725, 204100, 510300]
    tax_return = calc_income(myincome,mytax_list,myincome_list)
    print(tax_return)
elif tax_yr==2020:
    mytax_list = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]
    myincome_list=[9875, 40125, 85525, 163300, 207350, 518400]
    tax_return = calc_income(myincome,mytax_list,myincome_list)

    print(tax_return)
else:
    print("I don't know how to calculate tax for", tax_yr)

#for i in range (6):
#mytax_list = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]
#myincome_list=[9700, 39475, 84200, 160725, 204100, 510300]
