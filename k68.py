# Delete the element from given position
from array import *
a=array('i',[])
r=int(input(" Enter range or length of array : "))
print("-----------------------------------------------")
print(" Enter ",r," Elements for array : ")
print("-----------------------------------------------")
for i in range(r):
    print((i+1)," Element : ",end='')
    n=int(input())
    a.append(n)
print("----------------------------------------------")
print(" Array for elements are : ")
print(a)
po=int(input(" Enter the position : "))
po=po-1
for i in range(po,r-1):
    a[i]=a[i+1]
r=r-1
print(" After deleting the array elements are : ")
print(a)

