# Bubble sort
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
print("----------------------------------------------")
print(" Array for elements are : ")
print(a)
for i in range(r):
    for j in range(r-1):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print(" After bubble sorting ")
print(a)
