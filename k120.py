# method overloading
# calculator
def calculator(x,y):
    # process
    add=x+y
    sub=x-y
    mul=x*y
    div=x/y
    mod=x%y
    return add,sub,mul,div,mod
    # input
a=int(input(" Enter a : "))
b=int(input(" Enter b : "))
    # calling of function
add1,sub1,mul1,div1,mod1=calculator(a,b)
print(" add1 = ",add1)
print(" sub1 = ",sub1)
print(" mul1 = ",mul1)
print(" div1 = ",div1)
print(" mod1 = ",mod1)