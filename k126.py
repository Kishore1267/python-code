# class in G3
class G3():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def process(self):
        if self.a==self.b and self.a==self.c:
            print(" All are equal ")
        elif self.a>self.b and self.a>self.c:
            print(" A is greatest ")
        elif self.b>self.c:
            print(" B is greatest ")
        else:
            print(" C is greatest ")
# input
a=int(input(" Enter a : "))
b=int(input(" Enter b : "))
c=int(input(" Enter c : "))
obj=G3(a,b,c)
obj.process()

