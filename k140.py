# Hierarchial inheritance
class Radius():
    def __init__(self):
        self.r=float(input(" Enter radius : "))
    def displayr(self):
        print(" Radius = ",self.r)
class Diameter(Radius):
    def __init__(self):
        super(Diameter, self).__init__()
        self.d=2*self.r
    def displayd(self):
        print(" Diameter of a circle = ",self.d)
class Area(Radius):
    def __init__(self):
        super(Area, self).__init__()
        self.pi=3.14
        self.ar=self.pi*self.r*self.r
    def displayar(self):
        print(" Area of a circle = ",self.ar)
class Perimeter(Radius):
    def __init__(self):
        super(Perimeter, self).__init__()
        self.pi=3.14
        self.pe=2*self.pi*self.r
    def displaype(self):
        print(" Perimeter of a circle = ",self.pe)
obj=Diameter()
obj.displayd()
obj=Area()
obj.displayar()
obj=Perimeter()
obj.displaype()

