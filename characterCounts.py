import string

num = input("Enter a sentence: ")
countup = 0
countdown = 0
Digits = 0
count_Punctuatuions = 0
for i in num:
    if(i.islower()):
        countdown = countdown+1
    elif(i.isupper()):
        countup = countup+1
    elif(i.isdigit()):
        Digits = Digits+1
    elif i in string.punctuation:
        count_Punctuatuions = count_Punctuatuions+1
           
print('{:>15}'.format("Upper case"), '{:>5}'.format(countup))
print('{:>15}'.format("Lower case"), '{:>5}'.format(countdown))
print('{:>15}'.format("Digits"), '{:>5}'.format(Digits))
print('{:>15}'.format("Punctuation"), '{:>5}'.format(count_Punctuatuions))