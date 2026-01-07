#To use dates in python we need to import a module called datetime.
import datetime
x=datetime.datetime.now()
print(x)

#Returns year and weekday
import datetime
x=datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

#Creating own date
import datetime
x=datetime.datetime(2020,5,17) #here the datetime() works as a constructor(class)
print(x)


#there are many built in functions to use in the date or for strftime to print the date as we want.
