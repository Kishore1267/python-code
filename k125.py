# class
# Total & Average
class total():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def process(self):
        self.tot=self.a+self.b+self.c
        self.avg=self.tot/3
    def display(self):
        print(" Total = ",self.tot)
        print(" Average = ",self.avg)
# input
a=int(input(" Enter a : "))
b=int(input(" Enter b : "))
c=int(input(" Enter c : "))
obj=total(a,b,c)
obj.process()
obj.display()