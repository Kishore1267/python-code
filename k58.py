# Special number or not
n=int(input(" Enter number : "))
n1=n
sum=0
while(n>0):
    mod=n%10
    f=1
    for i in range(1,mod+1):
        f=f*i
    sum=sum+f
    n=n//10
if n1==sum:
    print(" Special number ")
else:
    print(" Not Special number ")

