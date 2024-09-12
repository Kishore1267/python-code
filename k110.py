# Without + return
def total():
    # input
    a=int(input(" Enter a : "))
    b=int(input(" Enter b : "))
    c=int(input(" Enter c : "))
    # process
    tot=a+b+c
    avg=tot/3
    return tot,avg
    # calling + display
tot1,avg1=total()
print(" Total = ",tot1)
print(" Average = ",avg1)
