#try-lets you test a block of code for errors.
#except-handles the error
try:
    print(x)  #raises an exception as x is not defined
except:
    print("An exception occured")


#many exceptions
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

#else:lets you execute code when there is no error.
#finally:executes code regardless of the try and except block
try:
    print("Hello")
except:
    print('Something went wrong')
else:
    print("Nothing went wrong")

#finally
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The try except is finished")


#raise an exception
x=-1
if x<0:
    raise Exception("Sorry, No NO below zero")



y="hello"
if not type(y) is int:
    raise TypeError("only integers are allowed")