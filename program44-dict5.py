#copy of one dict to another. It cant done like dict1=dict2.. its like assigning reference to the dict.
#1)Copy()
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year" : 1964
}
mydict=thisdict.copy()
print(mydict)

#2)dict()
mydict=dict(thisdict)
print(mydict)