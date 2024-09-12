class Electric_Bill():
    def __init__(self):
        self.name=str(input(" Enter name : "))
        self.add=str(input(" Enter address : "))
        self.month=str(input(" Enter month : "))
        self.cr=float(input(" Enter current reading : "))
        self.pr=float(input(" Enter previous reading : "))
    def process(self):
        self.ec=self.cr-self.pr
        if self.ec<=100:
            self.amt=self.ec*1
        elif self.ec<=200:
            self.amt=100*1+(self.ec-100)*2
        elif self.ec<=200:
            self.amt=100*1+100*2+(self.ec-200)*3
        else:
            self.amt=100*1+100*2+100*3+(self.ec-300)*4
    def display(self):
        print("--------------------------------------------------------")
        print("            Electric Bill for month                     ")
        print("--------------------------------------------------------")
        print("   Name                     = ",self.name)
        print("   Address                  = ",self.add)
        print("   Month                    = ",self.month)
        print("--------------------------------------------------------")
        print("   Current reading                        = ",self.cr)
        print("   Previous reading                       = ",self.pr)
        print("--------------------------------------------------------")
        print("    Electric consumption                  = ",self.ec)
        print("    Net                                   = ",self.amt)
        print("--------------------------------------------------------")
obj=Electric_Bill()
obj.process()
obj.display()
