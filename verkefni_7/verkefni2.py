# Your function definition goes here

user_input = input("Enter a string: ")

def count_case(string1):
    a = 0
    b = 0
    for i in range(len(string1)):
        if(string1[i].islower()):
            a +=1
        elif(string1[i].isupper()):
            b +=1
    return a, b
lower, upper = count_case(user_input)
# Call the function here

print("Upper case count: ", upper)
print("Lower case count: ", lower)