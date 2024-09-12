# Maximum number
from array import *
a=array('i',[])
r=int(input(" Enter range or length of array : "))
print("----------------------------------------------")
print(" Enter ",r," Elements for array : ")
print("----------------------------------------------")
for i in range(r):
    print((i+1)," Element : ",end='')
    n=int(input())
    a.append(n)
print("-----------------------------------------------")
print(" Array for elements are : ")
print(a)
max=a[0]
for i in range(r):
    if max<a[i]:
        max=a[i]
print(" Maximum number = ",max)
