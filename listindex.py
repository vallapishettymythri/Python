#index()-returns index of a particular element
#Index()-
lst=[3,4,4,5,6,7,7,7,8,9,15]
lst.index(15)



#Index using function
def my_index(lst,element):
    for i in range (len(lst)):
        if lst[i]==element:
            print(i)
lst=[3,4,4,5,6,7,7,7,8,9,15]
element=15
my_index(lst,element)




#Index using recursion
def my_index(lst,element,i):
    if i==len(lst):
        return []
    if lst[i]==element:
        return i
    return my_index(lst,element,i+1)
lst=[3,4,4,5,6,7,7,7,8,9,15]
element=6
my_index(lst,element,0)