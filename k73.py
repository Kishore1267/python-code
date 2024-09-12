# TRANSPOSE OF MATRIX
rr=int(input(" Enter row range : "))
cr=int(input(" Enter column range : "))
mat=[]
sn=1
# for initialize matrix
for row in range(rr):
    for col in range(cr):
        mat.append([0]*cr)
# for input matrix
print(" Enter ",(rr*cr)," Elements for MATRIX : ")
for row in range(rr):
    for col in range(cr):
        print(" Enter ",sn," Element : ",end='')
        mat[row][col]=int(input())
        sn=sn+1
# for display matrix
print(" MATRIX elements are : ")
for row in range(rr):
    for col in range(cr):
        print(mat[row][col],end=' ')
    print()
# TRANSPOSE OF MATRIX
print(" TRANSPOSE OF MATRIX elements are : ")
for row in range(rr):
    for col in range(cr):
        print(mat[col][row],end=' ')
    print()

