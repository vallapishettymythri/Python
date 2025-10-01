#Remove items- To remove and item, use the remove() or the discard() method.
thisset={"apple","banana","cherry"}
thisset.remove("banana")
thisset.discard("banana") #already removed not exist so it wont show anything.
print(thisset)

#.pop()- removes a random item from set.
x=thisset.pop()
print(x) #shows which value is removed
print(thisset)

#clear()-clears the set
thisset.clear()
print(thisset)

#del-deletes the set completely
