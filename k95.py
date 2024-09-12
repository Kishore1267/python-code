# List data sorted or not
a=[]
r=int(input(" Enter range for list elements : "))
for i in range(r):
    print(" Enter list elements : ",end='')
    n=int(input())
    a.append(n)
print(a)
flag=0
for i in range(r):
    for j in range(i+1,r-2):
        if a[i]>a[j]:
            flag=1
            break
print(" flag = ",flag)
if flag==0:
    print(" Half of the list data are sorted ")
else:
    print(" list data are not sorted ")
