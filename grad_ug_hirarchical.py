#we have a base class person, stores- name, age. Undergraduate, graduate, from person
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display1(self):
        print(self.name)
        print(self.age)
class undergraduate(person):
    def ug(self):
        self.display1()
class graduate(person):
    def g(self):
        self.display1()

p=undergraduate("Mythri",21)
p.ug()


p=graduate("Mayan",22)
p.g()