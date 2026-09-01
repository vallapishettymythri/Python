#Conversion of list into dictionary a way where index is value and value is key
lst=[3,4,5,6,7,8,9]
small={}
for i in range (len(lst)):
    small[lst[i]]=i
small