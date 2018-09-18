# is_prime function definition goes here

def is_prime(lala):
    for i in range(2, lala):
        if lala % i == 0:
            return False
    return True
     
num = int(input("Input an integer greater than 1: "))
prime = is_prime(num)
if prime:
    print(num, "is a prime")
else:
    print(num, "is not a prime")


# Call the function here and print out the appropriate message