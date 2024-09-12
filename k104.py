# Reverse number in functions(without argument)
def reverse():
    # input
    n=int(input(" Enter number : "))
    rev=0
    # process
    while(n>0):
        mod=n%10
        rev=rev*10+mod
        n=n//10
    # display
    print(" Reverse number as = ",rev)
reverse()