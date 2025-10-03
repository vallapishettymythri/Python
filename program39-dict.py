#Dictionaries- It is used to store data values in key:value pairs
#Ordered,changeable and do not allow duplicates.
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year" : 1964
}
print(thisdict)

#Duplicates will overwrite existing values.
thisdict1={
    "brand":"ford",
    "model":"mustang",
    "year" : 1964,
    "year" : 2005
}
print(thisdict1)

#Length of the dictionaries
print(len(thisdict))


#the values in dictionary can be of any data types.
dict1={
    "name":"john",
    "car":"mercedes",
    "colors":["red","orange","blue"]
    }
print(dict1)

#type shows the what type of the data type is it.
print(type(dict1))

#dict() constructor- It is also possible to use dict constructor() to make a dictionary.
dict2=dict(name="John",age=36,country="Norway")
print(dict2)