# sum of 1/1+1/2+1/3+1/4+-------->1/n
n=int(input(" Enter number : "))
sum=0
for i in range(1,n+1):
    sum=sum+1/i
print(" Sum = ",sum)
