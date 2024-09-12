# Power
b=int(input(" Enter base : "))
e=int(input(" Enter exponent : "))
po=1
for i in range(1,e+1):
    po=po*b
print(b,"^",e,"=",po)
