# Update tuple: Tuples are unchangeable or immutable. 
# Whenever we want to change a tuple we need to convert tuple to list update or remove and then again need to get back to tuple.
x=("apple","banana","cherry","kiwi","dragon","guava")
y=list(x)
y[1]="orange"
x=tuple(y)
print(x)

#add tuple to a tuple
z=("apple",)
x += z
print(x)

#Remove 
y=list(x)
y.remove("kiwi")
x=tuple(y)
print(x)


#delete-del function is used to delete the whole tuple.