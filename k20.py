# Sum as perfect number or Not Perfect
n=int(input(" Enter number : "))
sum=0
for i in range(1,n+1):
    if n%i==0:
        sum=sum+i
print(" Sum = ",sum)
if sum==n:
    print(" perfect number ")
else:
    print(" Not perfect number ")
