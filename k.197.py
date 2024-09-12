# write a python program for to find a factors a number
n=int(input(" Enter number : "))
count=0
for i in range(1,n+1):
    if n%i==0:
        count=count+1
print(n,"have",count,"factors")