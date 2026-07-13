#allows us to define a class that inherits all the methods and properties from another class.
#parent class: the class where all the properties are stored and inheroted from it. Its a base class.
#child class: derived class. It inherits from the parent class.
#create a parent class
class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
x=person("John","Doe")
x.printname()

#create child class
class student(person):
    pass
x=student("mike","will")
x.printname()

#we can use init function in the student class but its overides and doesnt inherits. 
#so we call the parent class again. 
#person__init__(self,fname,lname)
#or we can use super() function that will make the child class inherits all the methods and properties 
#from its parent class. 