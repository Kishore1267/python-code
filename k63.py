# Occurance number
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
print("-----------------------------------------------")
print(" Array for elements are : ")
print(a)
s=int(input(" Enter number to search : "))
count=0
po=array('i',[])
for i in range(r):
    if s==a[i]:
        count=count+1
        po.append(i+1)
if count==0:
    print(" Number not found ")
else:
    print(" Number found at ",count,'Times in following position ')
    for i in range(count):
        print(po[i])
