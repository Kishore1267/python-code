# Shift the element of list one step right
a=[]
r=int(input(" Enter range for list elements : "))
for i in range(r):
    print(" Enter list elements : ",end='')
    n=int(input())
    a.append(n)
print(a)
t=a[0]
for i in range(r-1):
    a[r-(i+1)]=a[i+1]
a[r-1]=t
print(" After shifting each right element : ",a)
