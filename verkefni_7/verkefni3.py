# The function definition goes here
def is_in_range(number):
    if number > 1 and number < 555:
        return True
    else:
        return False

num = int(input("Enter a number: "))

is_in_range(num)

result = is_in_range(num)
if result :
    print(num, "is in range.")
else :
    print(num, "is outside the range!")
# You call the function here