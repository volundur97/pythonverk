top_num = int(input("Input a number between 0 and 999: "))

sum = 0

for i in range(0,top_num):

    if i >0:
        digit = i % 10
        sum += digit ** 3
        i //= 10
        if top_num == sum:
            print(i)
        