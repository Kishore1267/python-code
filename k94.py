# Reverse the elements of list
a=[]
r=int(input(" Enter range for list elements : "))
for i in range(r):
    print(" Enter list elements : ",end='')
    n=int(input())
    a.append(n)
print(a)
b=0
e=r-1
while(b<=e):
    t=a[b]
    a[b]=a[e]
    a[e]=t
    b=b+1
    e=e-1
print(" List after reverse of elements are : ",a)



