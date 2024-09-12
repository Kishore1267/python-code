# With argument(Variable)
# G3
def G3(x,y,z):
    # process
    if x==y and x==z:
        print(" All are equal ")
    elif x>y and x>z:
        print(" X is greatest ")
    elif y>z:
        print(" Y is greatest ")
    else:
        print(" Z is greatest ")
    # input
a=int(input(" Enter a : "))
b=int(input(" Enter b : "))
c=int(input(" Enter c : "))
G3(a,b,c)
