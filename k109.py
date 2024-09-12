# With argument(Variable)
# reverse number
def reverse(n1):
    # process
    rev=0
    while(n1>0):
        mod=n1%10
        rev=rev*10+mod
        n1=n1//10
    # display
    print(" Reverse number as = ",rev)
    # input
n=int(input(" Enter number : "))
reverse(n)



