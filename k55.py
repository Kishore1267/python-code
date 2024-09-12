# Armstrong
n=int(input(" Enter number : "))
n1=n
sum=0
while(n>0):
    mod=n%10
    sum=sum+mod*mod*mod
    n=n//10
if n1==sum:
    print(" Armstrong ")
else:
    print(" Not Armstrong ")
    