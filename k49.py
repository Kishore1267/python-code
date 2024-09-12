r=int(input(" Enter range : "))
for row in range(1,r+1):
    for sp in range(1,r-row+2):
        print("  ",sep='',end='')
    for col in range(1,row+1):
        print(" ",col,sep='',end='')
    for k in range(row-1,0,-1):
        print(" ",k,sep='',end='')
    print()
    