class C_String():
    def __init__(self):
        self.str=str(input(" Enter string : "))
        self.len=len(self.str)
        print(" String = ",self.str)
        print(" Length = ",self.len)
    def reverse(self):
        print(" Reverse of string = ",self.str," = ",end='')
        for i in range(self.len-1,-1,-1):
            print(self.str[i],end='')
    '''        
    def pyramid(self):
        for row in range(self.len):
            for col in range(row+1):
                print(self.str[col],end=' ')
            print()
    '''
    '''
    def pyramid2(self):
        print("\n pyramid of ",str)
        for row in range(self.len):
            for col in range(self.len-row):
                print(self.str[col],end=' ')
            print()
    '''
    '''
    def pyramid3(self):
        for row in range(1,self.len+1):
            for col in range(1,self.len-row+2):
                print(" ",self.str[col],sep='',end='')
            print()
    '''
    def pyramid4(self):
        print("\n pyramid of string = ",self.str)
        for row in range(self.len):
            for sp in range(self.len-row+2):
                print("  ",sep='',end='')
            for col in range(row+1):
                print(" ",self.str[col],end=' ')
            print()
obj=C_String()
obj.reverse()
#obj.pyramid()
#obj.pyramid2()
#obj.pyramid3()
obj.pyramid4()

