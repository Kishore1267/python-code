# Prime number or not
n=int(input(" Enter number : "))
count=0
for i in range(1,n+1):
    if n%i==0:
        count=count+1
print(" Count = ",count)
if count==2:
    print(" prime number ")
else:
    print(" Not prime number ")
    