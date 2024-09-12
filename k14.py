# Square Root possible or not
import math

a=int(input(" Enter a : "))
b=int(input(" Enter b : "))
c=int(input(" Enter c : "))
d=b*b-4*a*c
print("d=",d)
if d>0:
    print(" Two different roots ")
    r1=(-b+math.sqrt(b)/2*a)
    r2=(-b-math.sqrt(b)/2*a)
    print(" Root 1 = ",r1)
    print(" Root 2 = ",r2)
elif d==0:
    print(" Same roots ")
    r1=r2=-b/2*a
    print(" Root 1 = ",r1)
    print(" Root 2 = ",r2)
else:
    print(" Roots are not possible ")
    