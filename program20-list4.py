#1)Remove specified item 
thislist=["apple","banana","cherry","orange","cherry","kiwi","melon","mango"]
thislist.remove("banana")
thislist.remove("cherry")  #this removes the first occurance of the duplicate.
print(thislist)

#2)Remove using specified index. Pop() is used.
thislist.pop(1)
thislist.pop() #doesnt specify index, removes the last element from the list.
print(thislist)

#3)del keyword - removes specified index too
del thislist[0]
#del thislist - deletes the list completely
print(thislist)

#4)clear the list- list is present but no content.
thislist.clear()
print(thislist)
