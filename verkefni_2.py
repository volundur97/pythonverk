x_str = input("Input x: ")
in_int = int(x_str)
# remember to convert to an int
first_three = in_int//1000
last_two = in_int%100
middle_two = (in_int//100)%100
print("original input:", x_str)
print("first_three:", first_three)
print("last_two:", last_two)
print("middle_two:", middle_two)
