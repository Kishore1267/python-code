# Single inheritance --> it enables to derived a class to inherit properties from a single parent class
class A():
    def __init__(self):
        self.a=int(input(" Enter a : "))
    def adisplay(self):
        print(" A = ",self.a)
class B(A):
    def __init__(self):
        super().__init__()
        self.b=int(input(" Enter b : "))
    def process(self):
        self.sum=self.a+self.b
    def bdisplay(self):
        print(" B = ",self.b)
        print(" Sum = ",self.sum)
obj=B()
obj.process()
obj.adisplay()
obj.bdisplay()


