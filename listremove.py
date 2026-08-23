#remove:removes an element from the list.
#Remove element using remove():
lst=[23,11,-22,56,12,67,-99,3]
lst.remove(11)
lst

#Remove element using func
def my_remove(lst,element):
    result=[]
    for i in lst:
        if i!=element:
            result.append(i)
    return result
lst=[23,11,-22,56,12,67,-99,3]
element=11
my_remove(lst,element)






#Remove element using rec
def my_remove(lst,element,i):
    if i==len(lst):
        return []
    
    if lst[i]==element:
        return my_remove(lst,element,i+1)
    return [lst[i]]+my_remove(lst,element,i+1)
lst=[23,11,-22,56,12,67,-99,3]
element=11
my_remove(lst,element,0)