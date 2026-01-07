#A file containing a set of functions that you wnat to include in your application.
#in simple words a module is nothing but a file containing code of functions variables etc. 

import mymodule  #created a file as mymodule.py and importing it.
mymodule.greeting("John")


#When using a function from the module use the syntax: module_name.function_name

import mymodule
a=mymodule.person1['age']
print(a)

#rename module as import module as mx
#we can use "from" to import a specific part from the module. 
from mymodule import person1
print (person1["age"])