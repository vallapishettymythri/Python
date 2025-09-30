#sort of the list. We use sort() method to sort the list items.
#It can sort alphabets and numerics.
#1)Sorting of alphabets
thislist=["orange","mango","kiwi","apple","banana","cherry"]
thislist.sort()
print(thislist)

#2)Sorting of numberals
no=[100,50,65,82,23]
no.sort()
print(no)

#3)sort descending- we will be using reverse=true.
thislist.sort(reverse=True)
print(thislist)


#4)numbericals descending
no.sort(reverse=True)
print(no)


#5)Customize sort function- We can customize the sort func by using key=function
def myfunc(n):
    return abs(n-50)
no.sort(key=myfunc)
print(no)


#6)Case Sensitive- automatically sort() method is case sensitive resulting in all captital letters being sorted before lower case.
list1=["banana","Orange","Kiwi","cherry"]
list1.sort()
list1.sort(key=str.lower)
print(list1)

#7)Reverse order
list1.reverse()
print(list1)