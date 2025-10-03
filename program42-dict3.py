#Remove Items
#1) Pop()
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year" : 1964
}
thisdict.pop("model")
print(thisdict)

#2)Popitem()-removes the last inserted item or a random one.
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year" : 1964
}
thisdict.popitem()
print(thisdict)

#3)Del-removes the item with the specified key name.
del thisdict["model"]
#it can even delete the dictionary completely.
print(thisdict)

#4)clear()-empties the dictionary
thisdict.clear()