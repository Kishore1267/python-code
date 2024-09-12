# Merge two array into third array
from array import *
a=array('i',[])
b=array('i',[])
c=array('i',[])
r1=int(input(" Enter range or length of array A : "))
print("-----------------------------------------------")
print(" Enter ",r1," Elements for array A : ")
print("-----------------------------------------------")
r2=int(input(" Enter range or length of array B : "))
print("-----------------------------------------------")
print(" Enter ",r2," Elements for array B : ")
print("-----------------------------------------------")
for i in range(r1):
    print((i+1)," Element A : ",end='')
    n=int(input())
    a.append(n)
print("----------------------------------------------")
print(" Array for elements are : ")
print(a)
for i in range(r2):
    print((i+1)," Element B : ",end='')
    n=int(input())
    b.append(n)
print("----------------------------------------------")
print(" Array for elements are : ")
print(b)
# Process of merging two elements
for i in range(r1):
    c.append(a[i])
for i in range(r2):
    c.append(b[i])
print(" After merging two elements are : ")
print(c)


