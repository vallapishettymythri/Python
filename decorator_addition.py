def decorator_addition(func): #func- alias 
    def wrapper(a,b):
        print(func(a,b)) #to print add functionality we use func(a,b)) which is alias of add
        print([2,3,4,5,6]+[10,11,12])
    return wrapper
@decorator_addition
def add(a,b):
    return a+b
add(5,6)