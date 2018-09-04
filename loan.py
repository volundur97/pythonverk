num = float(input("Input the cost of the item in $: "))
payment1 = 0.0
vextir = 0.0
greiddir_vextir = 0.0
upgreidir_vextir = 0.0
month = 0
count_month= 0

if num <=1000:
    vextir = 0.015
else:
    vextir = 0.02
while num > 1:
    
    if num * (vextir+1) >= 50:
        payment1 = 50.0
    else:
        payment1 = num * (vextir+1)
    upgreidir_vextir = num * vextir
    num += upgreidir_vextir -payment1
    month +=1
    print("Month: " + str(month) + " Payment: " + str(round(payment1 ,2)) + " Interest paid: " + str(round(upgreidir_vextir, 2)) + " Remaining debt: " + str(round(num, 2)))
    
    greiddir_vextir += upgreidir_vextir

print("\nNumber of months: " + str(month))
print("Total interest paid: " +str(round(greiddir_vextir, 2)))