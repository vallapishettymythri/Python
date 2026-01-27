#An inner class is a class defined isnide the another class. This inner class can access
#the properties and methods of outter class.
#inner classes are useful for grouping classes.
class Outer:
    def __init__(self):
        self.name="outer class"
    class Inner:
        def __init__(self):
            self.name="Inner class"
        def display(self):
            print("This is the inner class")
outer=Outer()
print(outer.name)
inner=outer.Inner()  #accesing inner class from the outer
inner.display()