# Your function definition goes here
def fibo(number):
    a = 0
    b = 1
    c = 0
    tala = "1 "
    for i in range(number-1):
        c = a + b
        tala += "{} ".format(c)
        a = b
        b = c
    return tala
n = int(input("Input the length of Fibonacci sequence (n>=1): "))
# Call your function here        
print(fibo(n))