print("Give me a word, a number, or them mixed and I will tell you if it is palindromic or not.")
word_or_number=input()
x=0
if (len(word_or_number))%2==0:
    j=(len(word_or_number))//2
else:
    j=(len(word_or_number))//2+1
for i in range(j):
   if not (word_or_number[i])==(word_or_number[len(word_or_number)-i-1]):
       print("This is not palindromic because", word_or_number[i], "is not", word_or_number[len(word_or_number)-i-1], end="")
       print(".")
       x=1
if x==0:
    print("This is palindromic.")
       
