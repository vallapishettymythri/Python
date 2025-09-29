#Accesing elements in the list.
#The elements in the list has the index for each element which makes to access them easily.
thislist=["apple","banana","orange","cherry","kiwi","melon","mango"]
print(thislist[1])

print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

#checking if element exist
if "apple" in thislist:
    print("Yes")