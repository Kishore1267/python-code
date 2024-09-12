# Local & Global variable
a=10
b=20
def func():
    a=100
    b=200
    print(" A = ",a)
    print(" B = ",b)
    a=a+1000
    b=b+1000
    print(" A = ",a)
    print(" B = ",b)
print(" A = ",a)
print(" B = ",b)
func()
