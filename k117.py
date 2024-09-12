# With + return
def G3(x,y,z):
    # process
    if x==y and x==z:
        return 0
    elif x>y and x>z:
        return x
    elif y>z:
        return y
    else:
        return z
    # input
a=int(input(" Enter a : "))
b=int(input(" Enter b : "))
c=int(input(" Enter c : "))
    # main
ans=G3(a,b,c)
if ans==0:
    print(" All numbers are equal ")
else:
    print(ans," is greatest number ")

