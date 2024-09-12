# Minimum number
from array import *
a=array('i',[])
r=int(input(" Enter range or length of array : "))
print("------------------------------------------------")
print(" Enter ",r," Elements for array : ")
print("------------------------------------------------")
for i in range(r):
    print((i+1)," Element : ",end='')
    n=int(input())
    a.append(n)
print("------------------------------------------------")
print(" Array for elements are : ")
print(a)
min=a[0]
for i in range(r):
    if min>a[i]:
        min=a[i]
print(" Minimum number = ",min)
