r=int(input(" Enter range : "))
for row in range(1,r+1):
    for col in range(1,r+1):
        if row==1 or col==1 or row==r or col==r:
            print("  *",sep='',end='')
        else:
            print("   ",sep='',end='')
    print()
    