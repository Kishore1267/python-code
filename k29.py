# Fibonacci series
r=int(input(" Enter range : "))
b=0
e=1
print(" Fibonacci series = ",b,"=",e,end='')
for i in range(1,r-1):
    sum=b+e
    print(",",sum,end='')
    b=e
    e=sum