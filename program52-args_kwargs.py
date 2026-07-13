#args and kwargs are used when we need to pass a unknown number of arguments.(tuples)
#arbitary arguments-*args 
#It is used when we don't kniw how many arguments will be passed in to the function. We add * bfore parameter name.
def my_func(*kids):
    print("the youngest child is " +kids[2])
my_func("emily","thomas","linus")

#*args- args parameter allows a func to accept any no of positional arguments.
def my_func(*args):
    print(type(args))
    print(args[0])
    print(args[1])
    print(args)
my_func("Emily","Thomas","Linus")

#using *args with regular arguments:
def my_func(greeting,*name):
    for name in name:
        print(greeting,name)
my_func("Hello","Emily","Thomas","John")

#arbitary keyword arguments-**kwargs- If you do not know how many keyword arguments will be passed in your function, add
#two asterisks. Dictionary!
def my_func(**myvar):
    print(type(myvar))
    print(myvar["name"])
    print(myvar["age"])
    print(myvar)
my_func(name="Thomas", age=30,city="Bergin")

#to combine args and kwargs there is an order to follow. 1)Regular paramenter, 2)*args 3)**kwargs

