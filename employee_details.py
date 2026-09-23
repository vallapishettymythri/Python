#show the employee details
class employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def display(self):
        print(self.id)
        print(self.name)
        print(self.salary)
obj=employee(101,"mythri","1C")
obj.display()