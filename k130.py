from array import *
class C_Array():
    def __init__(self):
        self.a=array('i',[])
        self.r=int(input(" Enter range or length of array : "))
        print("--------------------------------------------------")
        print(" Enter ",self.r," Elements for array : ")
        print("--------------------------------------------------")
        for i in range(self.r):
            print((i+1)," Element : ",end='')
            n=int(input())
            self.a.append(n)
    def process(self):
        self.tot=0
        self.avg=0
        for i in range(self.r):
            self.tot=self.tot+self.a[i]
        self.avg=self.tot/3
    def display(self):
        print(" Total = ",self.tot)
        print(" Average = ",self.avg)
obj=C_Array()
obj.process()
obj.display()

