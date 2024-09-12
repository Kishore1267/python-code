# Sum of Divisible by factorial and power
b=int(input(" Enter base : "))
e=int(input(" Enter exponent : "))
po=1
f=1
sum=1
for i in range(1,e+1):
    po=po*b
    f=f*i
    div=po/f
    sum=sum+div
print(" sum of divisible by factorial and power as = ",sum)