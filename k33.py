# col%2
r=int(input(" Enter range : "))
for row in range(1,r+1):
    for col in range(1,row+1):
        print(" ",col%2,sep='',end='')
    print()
    