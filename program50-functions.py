#functions is a block of code, which only runs when it is called.
#A function helps avoiding code repition.
#creating a function:
def greet():
  print("Hello from a function")

#calling a function
def my_func():
  print("Hello")
my_func()


#A function name must start with a letter or underscore OR numbers.
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

#return values
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

#you can use direct values 
def get_greeting():
  return "Hello"

print(get_greeting())

#pass function is used same when there is no matter in the function to avoid errors.
