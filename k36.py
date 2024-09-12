r=int(input(" Enter range : "))
x=1
for row in range(1,r+1):
    for col in range(1,row+1):
        print(" ",x,sep='',end='')
        x=x+1
    print()



