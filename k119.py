# method overloading
import math


def area(x=None, y=None, z=None):
    if y==None and z==None:
        ar=x*x
        print(" Side = ",x)
        print(" Area of square = ",ar)
    elif x!=None and y!=None and z==None:
        ar=(x*y)/2
        print(" Base = ",x)
        print(" Height = ",y)
        print(" Area of triangle = ",ar)
    elif x!=None and y!=None and z!=None:
        s=(a+b+c)/2
        ar=math.sqrt(s*(s-a)*(s-b)*(s-c))
        print(" a = ",x)
        print(" b = ",y)
        print(" c = ",z)
        print(" Area of triangle = ",ar)
# calling of function
s=int(input(" Enter side : "))
a=int(input(" Enter height : "))
b=float(input(" Enter base : "))
c=float(input(" Enter side : "))
area(s)
area(a,b)
area(a,b,c)


