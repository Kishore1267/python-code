# power in class
class power():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def process(self):
        self.po=1
        for i in range(1,self.y+1):
            self.po=self.po*self.x
    def display(self):
        print(self.x,"^",self.y,"=",self.po)
# input
b=int(input(" Enter base : "))
e=int(input(" Enter exponent : "))
obj=power(b,e)
obj.process()
obj.display()
