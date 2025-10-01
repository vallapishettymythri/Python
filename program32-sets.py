#sets- Unordered, unchangeable, and unindexed, doesn't allow duplicates.
#represented in {}
thisset={"apple","banana","cherry"}
print(thisset)

#if there are any duplicates duplicate values are ignored.
#true and 1 are considered same, false and 0 also. They print according to the first occurance.
thisset1={"apple","banana","cherry",1,True,False,0,2,"apple"}
print(thisset1)

#a set can contain different data types.
#len()
print(len(thisset1))

#type
print(type(thisset))
