# Factorial in functions(without argument)
def factor():
    # input
    n=int(input(" Enter number : "))
    f=1
    sum=1
    # process
    for i in range(1,n+1):
        f=f*i
        sum=sum+f
    # display
    print(" Factorial number as = ",n,"=",f)
    print("  Sum = ",sum)
factor()