#List Comprehension: It is a method to use for short-hand.
#1)For loop:
thislist=["apple","banana","cherry"]
[print(x)for x in thislist]

#2)Minimization of code:
newlist=[x for x in thislist if "a" in x]
print(newlist)

#3)condition use:
newlist=[x for x in thislist if x!="apple"]
print(newlist)


#4)No if statement:
newlist=[x for x in thislist]
print(newlist)


#5)Iterable: we will be using range to iterate.
newlist=[x for x in range(3)]
newlist=[x for x in range(3) if x<5]
print(newlist)

#6) Expression:
newlist=[x.upper() for x in thislist]
newlist=[x if x!="banana" else "orange" for x in thislist]
print(newlist)