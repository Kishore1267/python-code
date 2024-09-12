# Hybrid inheritance
class Student():
    def __init__(self):
        self.name=str(input(" Enter name : "))
        self.age=int(input(" Enter age   : "))
        self.roll=int(input(" Enter roll no.: "))
    def sdisplay(self):
        print(" Name = ",self.name)
        print(" Age  = ",self.age)
        print(" Roll no. = ",self.roll)
class Marks(Student):
    def __init__(self):
        super().__init__()
        self.m1=int(input(" Enter marks 1 : "))
        self.m2=int(input(" Enter marks 2 : "))
        self.m3=int(input(" Enter marks 3 : "))
    def mprocess(self):
        self.tot=self.m1+self.m2+self.m3
        self.per=(self.tot*100)/300
    def mdisplay(self):
        print(" M1 = ",self.m1)
        print(" M2 = ",self.m2)
        print(" M3 = ",self.m3)
        print(" Total = ",self.tot)
        print(" Percentage = ",self.per)
class Game():
    def __init__(self):
        super().__init__()
        self.gname=str(input(" Enter game name : "))
    def gdisplay(self):
        print(" Game name = ",self.gname)
class fees(Game,Marks):
    def __init__(self):
        super().__init__()
        self.famt=int(input(" Enter fees amount : "))
        self.fpaid=int(input(" Enter fees paid : "))
    def fprocess(self):
        self.bal=self.famt-self.fpaid
    def fdisplay(self):
        print(" fees amount = ",self.famt)
        print(" fees paid  = ",self.fpaid)
        print("--------------------------------")
        print(" Balance fees = ",self.bal)
        print("--------------------------------")
obj=fees()
obj.fprocess()
obj.fdisplay()
obj.mprocess()
obj.mdisplay()
obj.gdisplay()
obj.sdisplay()