 #Show the student details
class student:
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
    def display(self):
        
        print(self.rollno)
        print(self.name)
obj=student(101,"mythri")
obj.display()