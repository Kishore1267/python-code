# Reverse number
class reverse():
    def __init__(self,n1):
        self.n1=n1
    def process(self):
        self.rev=0
        while(self.n1>0):
            self.mod=self.n1%10
            self.rev=self.rev*10+self.mod
            self.n1=self.n1//10
    def display(self):
        print(" Reverse number as = ",self.rev)
# input
n=int(input(" Enter number : "))
obj=reverse(n)
obj.process()
obj.display()
