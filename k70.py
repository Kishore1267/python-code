# Selection sort
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
for i in range(r-1):
    for j in range(i+1,r):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(" After selection sorting ")
print(a)





