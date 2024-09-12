# class marksheet with input
class Mark():
    def __init__(self):
        self.name=str(input(" Enter name : "))
        self.age=int(input(" Enter age : "))
        self.roll=int(input(" Enter roll : "))
        self.m1=float(input(" Enter m1 : "))
        self.m2=float(input(" Enter m2 : "))
        self.m3=float(input(" Enter m3 : "))
        self.m4=float(input(" Enter m4 : "))
        self.m5=float(input(" Enter m5 : "))
        self.tot=0
    def process(self):
        self.tot=self.m1+self.m2+self.m3+self.m4+self.m5
        self.per=(self.tot*100)/500
        if self.per<=40:
            self.grade='E'
        elif self.per<=60:
            self.grade='D'
        elif self.per<=70:
            self.grade='C'
        elif self.per<=80:
            self.grade='B'
        else:
            self.grade='A'
    def display(self):
        print("-------------------------------------------------------")
        print("                     Marksheet                         ")
        print("-------------------------------------------------------")
        print("  Name                                     = ",self.name)
        print("  Age                                       = ",self.age)
        print("  Roll                                     = ",self.roll)
        print("-------------------------------------------------------")
        print("                     Subject Marks                     ")
        print("-------------------------------------------------------")
        print("  Hindi                                      = ",self.m1)
        print("  Mathematics                                = ",self.m2)
        print("  Computer                                   = ",self.m3)
        print("  English                                    = ",self.m4)
        print("  Science                                    = ",self.m5)
        print("-------------------------------------------------------")
        print("  Total                                     = ",self.tot)
        print("  Percentage                                = ",self.per)
        print("  Grade                                     = ",self.grade)
obj=Mark()
obj.process()
obj.display()

