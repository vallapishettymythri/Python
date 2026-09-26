#person, student, graduation
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display1(self):
        print(self.name)
        print(self.age)
class student(person):
    def __init__(self,name,age,rollno,grades):
        super().__init__(name,age)
        self.rollno=rollno
        self.grades=grades
    def display2(self):
        self.display1()
        print(self.rollno)
        print(self.grades)
class graduate_student(student):
    def __init__(self,name,age,rollno,grades,degree):
        super().__init__(name,age,rollno,grades)
        self.degree=degree
    def display3(self):
        self.display2()
        print(self.degree)
obj=graduate_student("abc",21,101,"A","Btech")