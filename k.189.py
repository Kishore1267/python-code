# write a python program for print 2 to 100 prime numbers
'''
Find total no of prime no between given range
also count the no of prime no
also find the sum of prime no
'''
r1=int(input(" Enter First Range  : "))
r2=int(input(" Enter second Range : "))
print(" Prime number between ",r1," to ",r2)
sum=0
pcount=0
for j in range(r1,r2+1):
    n=j
    count=0
    for i in range (1,n+1):
        if n%i==0:
            count=count+1
    if count==2:
        print(n)
        sum=sum+n
        pcount=pcount+1
print("-------------------------------")
print(" total no of prime no : ",pcount)
print(" sum prime no         : ",sum)
print("-------------------------------")