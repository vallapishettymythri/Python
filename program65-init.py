#init method is used in class to call the paaremters easily. 
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person("emily",36)
print(p1.name)
print(p1.age)


#default value. 
class person1:
    def __init__(self,name,age=18):
        self.name=name
        self.age=age
p1=person1("emily")
p2=person1("thomas",36)
print(p1.name,p1.age)
print(p2.name,p2.age)
