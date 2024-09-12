# factorial in class
class factor():
    def __init__(self,x):
        self.x=x
    def process(self):
        self.f=1
        for i in range(1,self.x+1):
            self.f=self.f*i
    def display(self):
        print(" Factorial number as = ",self.x,"=",self.f)
# input
n=int(input(" Enter number : "))
obj=factor(n)
obj.process()
obj.display()
