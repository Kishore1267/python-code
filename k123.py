# Recursion
def reverse(x,rev):
    if x==0:
        return rev
    else:
        mod=x%10
        rev=rev*10+mod
        x=x//10
        return reverse(x,rev)
# input
n=int(input(" Enter number : "))
ans=reverse(n,0)
print(" Reverse number as = ",ans)
