#Has constructor is overriding which constructure as we used 2 supers 
#2 bases its confused so we need to use class name and with self
class sample1:
    def __init__(self,name):
        self.name=name
    def display1(self):
        print(self.name)
class sample2:
    def __init__(self,age):
        self.age=age
    def display2(self):
        print(self.age)
class new_sample(sample1,sample2):
    def __init__(self,name,age,city):
        sample1.__init__(self,name)
        sample2.__init__(self,age)
        self.city=city
    def display(self):
        self.display1()
        self.display2()
        print(self.city)
obj1=new_sample("mythri",21,"hyd")