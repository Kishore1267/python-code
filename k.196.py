r=int(input(" Enter range : "))
k=r-1
for row in range(0, r):
    for sp in range(0, k):
        print(" ",end=' ')
    k=k-1
    for col in range(0, row+1):
        print("*  ",sep='',end=' ')
    print()

