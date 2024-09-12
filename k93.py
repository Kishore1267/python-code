# List --> List are used to store multiple items in a single variable
# Total & Average
a=[]
r=int(input(" Enter range for list elements : "))
for i in range(r):
    print(" Enter list elements : ",end='')
    n=int(input())
    a.append(n)
print(a)
tot=0
avg=0
for i in range(r):
    tot=tot+a[i]
avg=tot/r
print(" Total of list elements = ",tot)
print(" Average of list elements = ",avg)


