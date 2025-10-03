#Change items
#1
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year" : 1964
}
thisdict["year"]=2005
print(thisdict)

#2
thisdict.update({"year":2004})

print(thisdict)