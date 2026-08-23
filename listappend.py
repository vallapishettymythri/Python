#3.Append()- append is used to add a number into the end of the list.
#Append function
lst=[3,4,5,6,7,8,9]
lst.append(1000)
lst


#append-Using +(1)
def myappend(lst,element):
    return lst+[element]

lst=[3,4,5,6,7,8,9]
element=1000
myappend(lst,element)



#appending using loop
def myappend(lst,element):
    new_lst=[0]*(len(lst)+1)
    for i in range(len(lst)):
        new_lst[i]=lst[i]
    new_lst[-1]=element
    return new_lst
lst=[3,4,5,6,7,8,9]
element=1000
myappend(lst,element)




#using recursive
def append_recursive(lst,element):
    if len(lst)==0:
        return [element]
    else:
        return [lst[0]]+append_recursive(lst[1:],element)
lst=[3,4,5,6,7,8,9]
element=1000
append_recursive(lst,element)