#Join Sets- It has various methods in it. 
#1)Union()-Joins both the sets.
set1={"apple","banana","cherry"}
set2={"mango","dragon","guava","apple"}
set3=set1.union(set2)
set3=set1 | set2  #| symbol is used for union
print(set3)


#2)update()-adds
set1.update(set2)
print(set1)

#3)intersection()
set3=set1.intersection(set2)
#set3=set1 & set2
print(set3)

#4)difference()-not present items in one set
set3=set1.difference(set2)
print(set3)

#5)Symmentric_difference()-keeps elements that are not present in both sets
set3=set1.symmetric_difference(set2)
print(set3)

