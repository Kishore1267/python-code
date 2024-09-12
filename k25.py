# Sum of Factorial as 1 + 1! +2! +3! +4!-------->!n
n=int(input(" Enter number : "))
f=1
sum=1
for i in range(1,n+1):
    f=f*i
    sum=sum+f
print(" Sum of factorial as = ",sum)
