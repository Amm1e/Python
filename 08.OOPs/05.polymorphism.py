class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addPoint(self, p):
        return Point((self.x + p.x), (self.y + p.y))
    
    def printPoint(self):
        print(f"X is {self.x}, Y is {self.y}")

# overloading + operator
    def __add__(self,p):
        return Point((self.x + p.x), (self.y + p.y))
    
p1 = Point(3,2)
p2 = Point(4,5)
p3 = p1.addPoint(p2)
p3.printPoint()
p4=p1+p2#will give error until we overload + operator
p4.printPoint()

