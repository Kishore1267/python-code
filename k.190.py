# write a python program for reverse all the array elements
from array import *
a=array('i',[])
r=int(input(" Enter range or length of array : "))
print("-------------------------------------------------")
print(" Enter ",r," Elements for array : ")
print("-------------------------------------------------")
for i in range(r):
    print((i+1)," Element : ",end='')
    e=int(input())
    a.append(e)
print("------------------------------------------------")
print(" Array for elements are : ")
print(a)
for i in range(r):
    n=a[i]
    rev=0
    while(n>0):
        mod=n%10
        rev=rev*10+mod
        n=n//10
    print(rev)
