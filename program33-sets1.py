#Access items- We can't access items using index. 
# We need to use for loop or in keyword to know whether a value is present.
thisset={"apple","banana","cherry"}
for x in thisset:
    print(x)

print("cherry" in thisset)
print("cherry" not in thisset)

#Change items- We can't change a set once it is created. We can add new items!
