#WAP using class to find the area of rectangle
class rectanglearea:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        arearec=self.length*self.breadth
        print("area:",arearec)
rec=rectanglearea(2,3)
rec.area()