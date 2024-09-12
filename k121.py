# Recursion
def factor(x):
    # process
    if x==1:
        return x
    else:
        return x*factor(x-1)
    # input
n=int(input(" Enter number : "))
ans=factor(n)
print(" Factorial number as = ",n,"=",ans)
