# Neon
n=int(input(" Enter number : "))
ns=n*n
sum=0
while(ns>0):
    mod=ns%10
    sum=sum+mod
    ns=ns//10
if n==sum:
    print(" Neon ")
else:
    print(" Not Neon ")
    