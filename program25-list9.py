#Join or concatenate 2 lists.
#1)Using + symbol we can concatenate 2 lists.
list1=["a","b","c"]
list2=[1,2,3]
list3=list1+list2
print(list3)


#2)using append()
for x in list2:
    list1.append(x)
    print(list1)

#3)using extend()
list1.extend(list2)
print(list1)

