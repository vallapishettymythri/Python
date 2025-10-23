#Scope is a variable only avaiable inside the region it is created.
#Local Scope: Created inside a function, only used by that function.
def myfunc():
    x=300
    print(x)
myfunc()

#func inside func
def myfunc():
    x=300
    def myinner():
        print(x)
    myinner()
myfunc()

#global scope- can be used with any scope or any function
x=300
def myfunc():
    print(x)
myfunc()
print(x)

#naming variables-if opearting with the same variable name inside and outside of a function, it treaats
#them as two seperate variables.
x=300
def myfunc():
    x=200
    print(x)
myfunc()
print(x)

#global keyword-the global key word makes a variable global.
def myfunc():
    global x
    x=300
myfunc()
print(x)
