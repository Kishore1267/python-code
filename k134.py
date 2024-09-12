class Salary():
    def __init__(self):
        self.name=str(input(" Enter name : "))
        self.add=str(input(" Enter address : "))
        self.post=str(input(" Enter post : "))
        self.month=str(input(" Enter month : "))
        self.bs=float(input(" Enter basic salary : "))
    def process(self):
        self.da=(80*self.bs)/100
        self.ta=(15*self.bs)/100
        self.hra=(15*self.bs)/100
        self.pf=(15*self.bs)/100
        self.esi=(15*self.bs)/100
        if self.bs<=1000:
            self.tax=0
        elif self.bs<=2000:
            self.tax=(self.bs*10)/100
        else:
            self.tax=(self.bs*20)/100
        self.sum=self.da+self.ta+self.hra
        self.sub=self.pf+self.esi+self.tax
        self.net=self.bs+self.sum-self.sub
    def display(self):
        print("-----------------------------------------------------------")
        print("                  SALARY SLIP FOR MONTH                    ")
        print("-----------------------------------------------------------")
        print("  NAME                                         = ",self.name)
        print("  ADDRESS                                      = ",self.add)
        print("  POST                                         = ",self.post)
        print("-----------------------------------------------------------")
        print("                      BASIC SALARY               = ",self.bs)
        print("-----------------------------------------------------------")
        print(" DA                                            = ",self.da)
        print(" TA                                            = ",self.ta)
        print(" HRA                                           = ",self.hra)
        print("-----------------------------------------------------------")
        print(" Sum          = ",self.sum,"Sub",self.sub)
        print(" Net          = ",self.net)
        print("-----------------------------------------------------------")
obj=Salary()
obj.process()
obj.display()
