# Insert the element at given position
a=[]
r=int(input(" Enter range for list elements : "))
for i in range(r):
    print(" Enter list elements : ",end='')
    n=int(input())
    a.append(n)
print(a)
po=int(input(" Enter the position : "))
v=int(input(" Enter the value : "))
a.append(None)# This will create one more element at the end given position
for i in range(po,r-1):
    a[i]=a[i-1]
a[po]=v
print(" After inserting the new element in the given position ",a)

