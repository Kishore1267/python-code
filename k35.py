# Reverse number in while loop
n=int(input(" Enter number : "))
rev=0
while(n>0):
    mod=n%10
    rev=rev*10+mod
    n=n//10
print(" Reverse number as while loop = ",rev)
