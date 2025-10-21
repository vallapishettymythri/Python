#Added inside the function, inside parenthesis. Can add as many arguments as needed.
#one argument
def func(fname):
    print(fname+ " is my friend")
func("Emily")

#no.of.arguments
def my_func(fname,lname):
    print(fname+ " "+lname)

my_func("Abdul", "Kalam") #if it has 2 arguments need to use the both arugemts or else it doesn't take.

#parameters-it is variable listed inside the parenthesis. Assign default parameters.When there is no parameter call, it takes default. 
def my_func(name="friend"):
    print("Hello", name)
my_func("emil")
my_func()

#keyword argument-Key=Value Syntax
def func(animal,name):
    print("I have a", animal)
    print("My", animal+ "is name is ", name)
func(animal="dog",name="buddy")
#The order doesn't matter
#the way of calling arguments normally are called positional arguments. Order matters.
#we can pass different types of data types.
#return values
def func(x,y):
    return x+y
result= func(5,3)
print(result)


