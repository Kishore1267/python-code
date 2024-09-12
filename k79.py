# Backward Diagonal
rr = int(input(" Enter row range : "))
cr = int(input(" Enter column range : "))
a=[]
sn=1
# Initialize matrix
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
sn=1
# for display matrix
print(" MATRIX of elements are : ")
for row in range(rr):
    for col in range(cr):
        print(a[row][col],end=' ')
    print()
print(" Backward diagonal ")
sum=0
for row in range(rr):
    for col in range(cr):
        if row+col==2:
            print(a[row][col],end=' ')
            sum=sum+a[row][col]
        else:
            print("  ",end='')
    print()
print("------------------------------------------")
print(" Sum = ",sum)
print("------------------------------------------")

