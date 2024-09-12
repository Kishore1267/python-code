# Multilevel inheritance -->
      # It is a type of inheritance that involves inheriting a class that has already inherited some other class.
class A():
    def __init__(self):
        self.a=int(input(" Enter a : "))
    def adisplay(self):
        print(" A = ",self.a)
class B(A):
    def __init__(self):
        super(B, self).__init__()
        self.b=int(input(" Enter b : "))
    def bdisplay(self):
        print(" B = ",self.b)
class C(B):
    def __init__(self):
        super(C, self).__init__()
        self.c=int(input(" Enter c : "))
    def process(self):
        self.tot=0
        self.avg=0
        self.tot=self.a+self.b+self.c
        self.avg=self.tot/3
    def cdisplay(self):
        print(" Total = ",self.tot)
        print(" Average = ",self.avg)
obj=C()
obj.process()
obj.adisplay()
obj.bdisplay()
obj.cdisplay()
