# With + return
def total(x,y,z):
    # process
    tot=x+y+z
    avg=tot/3
    return tot,avg
    # input
a=int(input(" Enter a : "))
b=int(input(" Enter b : "))
c=int(input(" Enter c : "))
    # calling + display
tot1,avg1=total(a,b,c)
print(" Total = ",tot1)
print(" Average = ",avg1)
