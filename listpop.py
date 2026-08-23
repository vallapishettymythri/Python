#pop- removes the element of an index
#Pop()
lst=[23,11,-22,56,12,67,-99,3]
lst.pop(4)
lst


#Pop using function 
def my_pop(lst,index):
    value=lst[index]
    result=[]
    for i in lst:
        if i!=value:
            result.append(i)
    return value, result
lst=[23,11,-22,56,12,67,-99,3]
index=4
my_pop(lst,index)



#pop using recursion
def my_pop(lst,index,i):
    if i==len(lst):
        return []
    if i==index:
        return my_pop(lst,index,i+1)
    return [lst[i]]+my_pop(lst,index,i+1)
lst=[23,11,-22,56,12,67,-99,3]
index=int(input("index:"))
my_pop(lst,index,0)