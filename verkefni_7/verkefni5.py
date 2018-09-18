# palindrome function definition goes here
import string
def palindrome(lala):
    racecar = string.punctuation + string.whitespace
    string1 = ""
    for i, l in enumerate(lala):
        if l not in racecar: 
            string1 += l.lower()

    if string1 ==string1[::-1]:
        return True
    else:
        return False

in_str = input("Enter a string: ")
palindrome_1 = palindrome(in_str)
if palindrome_1:
    print("\"{}\" is a palindrome.".format(str(in_str)))        
else:
    print("\"{}\" is not a palindrome.".format(str(in_str)))


        






# call the function and print out the appropriate message