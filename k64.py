# Binary Search --> Data should be sorted order
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
s=int(input(" Enter number to search : "))
po=0
b=0
e=r-1
while(b<=e):
    mid=(b+e)//2
    if s==a[mid]:
        po=mid+1
        break
    elif s>a[mid]:
        b=mid+1
    else:
        e=mid-1
if po==0:
    print(" Number not found ")
else:
    print(" Number found at ",po,'Times in following position')

