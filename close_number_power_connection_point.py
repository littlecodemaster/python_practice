print("Give me a number 'a' and I will tell you the first number 'n' such that a^(n+1)<=(a+1)^n.")
a=int(input())
b=0
while (a**(b+1))>((a+1)**b):
    b=b+1
print(b)
