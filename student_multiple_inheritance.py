#problem for students which stores and prints academics and extracurricular activities
class academic:
    def __init__(self,grades,subjects):
        self.grades=grades
        self.subjects=subjects
    def display1(self):
        print(self.grades)
        print(self.subjects)
class extracurricular:
    def __init__(self,activities,awards):
        self.activities=activities
        self.awards=awards
    def display2(self):
        print(self.activities)
        print(self.awards)
class student(academic,extracurricular):
    def __init__(self,grades,subjects,activities,awards):
        academic.__init__(self,grades,subjects)
        extracurricular.__init__(self,activities,awards)
    def display(self):
        self.display1()
        self.display2()
st=student("A","Math","Badminton","Chess player")