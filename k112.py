# Without + return
def power():
    # input
    b=int(input(" Enter base : "))
    e=int(input(" Enter exponent : "))
    po=1
    # process
    for i in range(1,e+1):
        po=po*b
    return po
    # calling + display
po1=power()
print(" Power as = ",po1)
