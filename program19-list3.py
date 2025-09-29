#Append- Adding elements to the end of the list.
thislist=["apple","banana","orange"]
thislist.append("cherry")
print(thislist)

#extend()-Used to add one list to another list by extending one whole list.
more=["mango","cherry","dragon"]
thislist.extend(more)
print(thislist)
#extend doesn't only works with list to list but we can use any of the built-in types to extend.
