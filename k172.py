# Binary to decimal
import math

n = int(input(" Enter number : "))
sum = 0
i = 0
while(n>0):
    mod=n%10
    sum=int(sum+mod*math.pow(2,i))
    i=i+1
    n=n//10
print(" Sum = ",sum)