#Copy-copies the list
lst=[23,11,-22,56,12,67,99,3]
lst1=[]
lst1=lst.copy()
lst1



#copy using func
def copying(lst1):
    lst2=[0]*len(lst1)
    for i in range(len(lst1)):
        lst2[i] = lst1[i]
    return lst2
lst=[23,11,-22,56,12,67,99,3]
copying(lst1)