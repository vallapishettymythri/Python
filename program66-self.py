#self parameter is a reference to the current instance of the class
#it is used to access class properties and methods
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print("Hello I'am"+self.name)
p1=person("Emil",25)
p1.greet()


class car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def display(self):
        print(f"{self.year}{self.brand}{self.year}")
car1=car("toyota","corolla",2020)
car1.display()        