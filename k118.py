# With + return
def reverse(n1):
    # process
    rev=0
    while(n1>0):
        mod=n1%10
        rev=rev*10+mod
        n1=n1//10
    return rev
    # input
n=int(input(" Enter number : "))
    # calling + display
rev1=reverse(n)
print(" Reverse number as = ",rev1)
