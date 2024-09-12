r=int(input(" Enter range : "))
for row in range(1,r+1):
    for sp in range(1,row+1):
        print("  ",sep='',end='')
    for col in range(1,r-row+2):
        print("   ",col,sep='',end='')
    print()
