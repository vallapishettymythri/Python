#copy of one list to another: list1=list2 doesn't mean copying its refering!
#1)Copy():
thislist=["orange","mango","kiwi","apple","banana","cherry"]
list1=thislist.copy()
print(list1)

#2)list():
list1=list(thislist)
print(list1)


#3)slice(:):
list1=thislist[:]
print(list1)
