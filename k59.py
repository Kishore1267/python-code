# Automorphic
import math

n=int(input(" Enter number : "))
ns=n*n
n1=n
count=0
while(n>0):
    count=count+1
    n=n//10
div=math.pow(10,count)
if n1==ns%10:
    print(" Automorphic ")
else:
    print(" Not Automorphic ")
