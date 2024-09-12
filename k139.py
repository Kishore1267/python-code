# Multiple inheritance -->
    # When a class is derived from more than one base class
class A():
    def __init__(self):
        self.a=int(input(" Enter a : "))
    def adisplay(self):
        print(" A = ",self.a)
class B():
    def __init__(self):
        super(B, self).__init__()
        self.b=int(input(" Enter b : "))
    def bdisplay(self):
        print(" B = ",self.b)
class C(B,A):
    def __init__(self):
        super(C, self).__init__()
        self.c=int(input(" Enter c : "))
    def cprocess(self):
        self.tot=0
        self.avg=0
        self.tot=self.a+self.b+self.c
        self.avg=self.tot/3
    def cdisplay(self):
        print(" Total = ",self.tot)
        print(" Average = ",self.avg)
obj=C()
obj.cprocess()
obj.adisplay()
obj.bdisplay()
obj.cdisplay()