my_int = int(input('Give me an int >= 0: '))
# Fill in the missing code
bstr = ""
staðann = 0
tala = my_int
if my_int > 0:
    while tala >0:
        staðann = tala % 2
        tala = tala //2
        bstr += str(staðann)
else:
    bstr += "0"
bstr = bstr[::-1]
print("The binary of", my_int, "is", bstr)

