num = int(input("Initial value: "))
num1 = int(input("Step: "))
counter = num1
sum = num

while sum <=100:
    print (num, end=' ')
    num = num + counter
    sum += num
    
print("Sum of series:", sum)
