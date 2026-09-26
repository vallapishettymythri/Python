#Single inheritance
class base_class:
    def __init__(self):
        print("parent class constructor")
    def display(self):
        print("thank you!!")
class derived_class(base_class):
    def display2(self):
        print("hello")
obj=derived_class()

