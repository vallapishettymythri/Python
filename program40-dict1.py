#Accessing Items- 
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year" : 1964
}
x=thisdict["model"]
print(x)
#or we can use get()
x=thisdict.get("model")
print(x)

#keys()-returns a list if all keys in the dictionary
x=thisdict.keys()
print(x)

#add new item
thisdict["color"]="red" 
print(thisdict)

#values()-used to get the values
x=thisdict.values()
print(x)

#can update
thisdict["year"]=2005
print(thisdict)

#items()- returns each item in a dictionary as tuples in a list
x=thisdict.items()
print(x)

#check if key exists
if "model" in thisdict:
    print("Yes!")
