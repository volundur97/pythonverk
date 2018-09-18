num = input("Enter a month: ")
num1 = input("Enter a day: ")
holyday = num==("december") + num1==("25")
first_day = num=("january") + num1=("1")
nationalday= num=("june") + num1=("17")

if num == holyday:
    print("Month:", num)
    print("Day: ", num1)
    print("Christmans day")
if num == first_day:
    print("Month: ", num)
    print("Day: ", num1)
    print("New year's day")
if num == nationalday:
    print("Month: ", num)
    print("Day: ", num1)
    print("National holiday")
else:
    print("Month: ", num)
    print("Day: ", num1)
    print("Not a holiday") 


    



 