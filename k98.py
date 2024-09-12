# Remove the element from given position as list
a=[]
r=int(input(" Enter range for list elements : "))
for i in range(r):
    print(" Enter list elements : ",end='')
    n=int(input())
    a.append(n)
print(a)
po=int(input(" Enter the position : "))
po=po-1
for i in range(po,r-1):
    a[i]=a[i+1]
a.pop()
print(" After removing the elements of list are : ",a)
