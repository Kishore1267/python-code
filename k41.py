r=int(input(" Enter range : "))
for row in range(1,r+1):
    for col in range(1,r-row+2):
        print("  ",col,sep='',end='')
    print()
    


    