#  sum of power
b=int(input(" Enter base : "))
e=int(input(" Enter exponent : "))
po=1
sum=1
for i in range(1,e+1):
    po=po*b
    sum=sum+po
print(" Sum of power as = ",sum)

