# Multiplication of Matrix
rr=int(input(" Enter row range : "))
cr=int(input(" Enter column range : "))
a=[]
b=[]
c=[]
sn=1
# Initialize matrix
for row in range(rr):
    a.append([0]*cr)
for row in range(rr):
    b.append([0]*cr)
for row in range(rr):
    c.append([0]*cr)
# for input matrix A
print(" Enter ",(rr*cr)," Elements for MATRIX A : ")
for row in range(rr):
    for col in range(cr):
        print(" Enter ",sn," Element A : ",end='')
        a[row][col]=int(input())
        sn=sn+1
sn=1
# for input matrix B
print(" Enter ",(rr*cr)," Elements for MATRIX B : ")
for row in range(rr):
    for col in range(cr):
        print(" Enter ",sn," Element B : ",end='')
        b[row][col]=int(input())
        sn=sn+1
sn=1
# for display matrix A
print(" MATRIX of element A are : ")
for row in range(rr):
    for col in range(cr):
        print(a[row][col],end=' ')
    print()
# for display matrix B
print(" MATRIX of element B are : ")
for row in range(rr):
    for col in range(cr):
        print(b[row][col],end=' ')
    print()
print(" Multiplication of matrix A & B are : ")
for row in range(rr):
    for col in range(cr):
        c[row][col]=0
        for k in range(rr):
            c[row][col]=c[row][col]+a[row][k]*b[k][col]
        print(" ",c[row][col],end='')
    print()







