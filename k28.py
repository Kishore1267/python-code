# sum of divisible by factorial and power as 1 - x^1/factorial 1 _______-x^n
b=int(input(" Enter base : "))
e=int(input(" Enter exponent : "))
po=1
f=1
sum=1
for i in range(1,e+1):
    po=po*b
    f=f*i
    div=po/f
    if i%2==0:
        sum=sum+div
    else:
        sum=sum-div
print(" Sum = ",sum)
