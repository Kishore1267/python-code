# Decimal to Binary -->proof 1010
from array import *
a=array('i',[])
n=int(input(" Enter number : "))
i=0
while(n>0):
    mod=n%2
    a.append(mod)
    i=i+1
    n=n//2
print(" i = ",i)
for j in range(i-1,-1,-1):
    print(a[j],end='')

