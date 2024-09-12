# MATRIX Base program
rr=int(input(" Enter row range : "))
cr=int(input(" Enter column range : "))
a=[]
sn=1
# for initialize matrix
for row in range(rr):
    for col in range(cr):
        a.append([0]*cr)
# for input matrix
print(" Enter ",(rr*cr)," Elements for MATRIX : ")
for row in range(rr):
    for col in range(cr):
        print(" Enter ",sn," Element : ",end='')
        a[row][col]=int(input())
        sn=sn+1
# for display matrix
print(" MATRIX elements are : ")
for row in range(rr):
    for col in range(cr):
        print(a[row][col],end=' ')
    print()
    