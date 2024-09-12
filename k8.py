# greatest among 3
a=int(input(" Enter a : "))
b=int(input(" Enter b : "))
c=int(input(" Enter c : "))
if a==b and a==c:
    print(" All are equal ")
elif a>b and a>c:
    print(" A is greatest ")
elif b>c:
    print(" B is greatest ")
else:
    print(" C is greatest ")
    