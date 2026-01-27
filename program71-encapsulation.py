#encapsulation is about protecting data inside a class. Hides the internal details.
#Private property- uses __prefix
class person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age #private
p1=person("emil",25)
print(p1.name)
print(p1.__age) #error

#to get 
def get_age(self):
    return self.__age
p1 = Person("Tobias", 25)
print(p1.get_age()) #sets private property value

#the encapsulation is used for data protection, validation, flexibility, controlled
