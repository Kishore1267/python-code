# Up
r=int(input(" Enter range : "))
for row in range(1,r+1):
    for sp in range(1,row+1):
        print("  ",sep='',end='')
    for col in range(1,r-row+2):
        if col==1 or col==r-row+1:
            print("   *",sep='',end='')
        else:
            print("    ",sep='',end='')
    print()
# Down
for row in range(2,r+1):
    for sp in range(1,r-row+2):
        print("  ",sep='',end='')
    for col in range(1,row+1):
        if col==1 or col==row:
            print("   *",sep='',end='')
        else:
            print("     ",sep='',end='')
    print()

