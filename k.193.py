# write a python program for array elements in prime numbers
from array import*
a=array('i',[])
r=int(input(" Enter range or length of array : "))
print("------------------------------------------------")
print(" Enter ",r," Elements for array : ")
print("------------------------------------------------")
for i in range(r):
    print((i+1)," Element : ",end='')
    n=int(input())
    a.append(n)
print("-----------------------------------------------")
print(" Array for elements are : ")
print(a)
for i in range(r):
    n=a[i]
    count=0
    for j in range (1,n+1):
        if n%j==0:
            count=count+1
    if count==2:
        print(n)
