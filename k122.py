# power in recursion
def power(x,y):
    # process
    if y==1:
        return x
    else:
        return x*power(x,y-1)
# input
b=int(input(" Enter base : "))
e=int(input(" Enter exponent : "))
ans=power(b,e)
print(b,"^",e,"=",ans)

