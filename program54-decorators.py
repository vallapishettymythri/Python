# decorators are nothing but adding extra behavior to a function.

def changecase(func):   # decorator function 
    def myinner():
        return func().upper()
    return myinner

@changecase  # calling the decorator
def myfunc():
    return "Hello"

print(myfunc())


# a decorator can be called multiple times.
def changecase(func):    
    def myinner():
        return func().upper()
    return myinner

@changecase  # calling the decorator
def myfunc():
    return "Hello"
print(myfunc())

@changecase
def otherfunc():
    return "I am sorry!"

print(myfunc())
print(otherfunc())


# arguments in the decorated function can also be decorated.
def changecase(func):   # decorator function 
    def myinner(x):   # wrapper func
        return func(x).upper()
    return myinner

@changecase  # calling the decorator
def myfunc(nam):
    return "Hello " + nam
print(myfunc("John"))


# args and kwargs: 
def changecase(func):   # decorator function 
    def myinner(*args, **kwargs):   # wrapper func
        return func(*args, **kwargs).upper()
    return myinner

@changecase  # calling the decorator
def myfunc(nam):
    return "Hello " + nam
print(myfunc("John"))


# Metadata - a way of calling the output. We use it as __name__
def myfunc():
    return "Have a great day!"
print(myfunc.__name__)
