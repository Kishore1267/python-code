# Insert
from array import *
a=array('i',[])
r=int(input(" Enter range or length of array : "))
print("--------------------------------------------")
print(" Enter ",r," Elements for array : ")
print("--------------------------------------------")
for i in range(r):
    print((i+1)," Element : ",end='')
    n=int(input())
    a.append(n)
print("--------------------------------------------")
print(" Array for elements are : ")
print(a)
po=int(input(" Enter the position : "))
v=int(input(" Enter the value : "))
po=po-1
a.append(0)
for i in range(r,po,-1):
    a[i]=a[i-1]
a[po]=v
print(" After insertion sorting ")
print(a)
