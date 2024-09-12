# Power in functions(without argument)
def power():
    # input
    b=int(input(" Enter base : "))
    e=int(input(" Enter exponent : "))
    po=1
    sum=1
    # process
    for i in range(1,e+1):
        po=po*b
        sum=sum+po
    # display
    print(b,"^",e,"=",po)
power()