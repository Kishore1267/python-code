# Linear search
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
print("---------------------------------------------")
print(" Array for elements are : ")
print(a)
s=int(input(" Enter number to search : "))
po=0
for i in range(r):
    if s==a[i]:
        po=i+1
        break
if po==0:
    print(" Number not found ")
else:
    print(" Number found at ",po,'Times in following position ')

