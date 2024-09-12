class Atm():
    def __init__(self):
        self.name=str(input(" Enter name : "))
        self.ac=int(input(" Enter account no . : "))
        self.bal=int(input(" Enter balance amount : "))
    def process(self):
        print(" 1. Deposit ")
        print(" 2. Withdrawal ")
        print(" 3. Amount ")
        self.ch=int(input(" Enter your choice : "))
        if self.ch==1:
            self.d=int(input(" Enter your deposit : "))
            self.bal=self.bal+self.d
            print(" Balance amount = ",self.bal)
        elif self.ch==2:
            if self.bal<1000:
                print(" Insufficient Balance ")
            else:
                self.w=int(input(" Enter your withdrawal : "))
                self.bal=self.bal-self.w
                print(" Balance amount = ",self.bal)
        else:
            print(" Balance amount = ",self.bal)
obj=Atm()
obj.process()
