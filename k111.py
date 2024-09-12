# Without + return
def factor():
    # input
    n=int(input(" Enter number : "))
    f=1
    # process
    for i in range(1,n+1):
        f=f*i
    return f
    # calling + display
f1=factor()
print(" factorial number as = ",f1)
