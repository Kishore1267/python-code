def G3():
    # input
    a=int(input(" Enter a : "))
    b=int(input(" Enter b : "))
    c=int(input(" Enter c : "))
    # process
    if a==b and a==c:
        print(" All are equal ")
    elif a>b and a>c:
        print(" A is greatest ")
    elif b>c:
        print(" B is greatest ")
    else:
        print(" C is greatest ")
    # main
G3()