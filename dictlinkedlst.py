#Using for loop
def linked_list(lst):
    ll={
        "data":lst[0],
        "link":None
    }
    tmp=ll
    for i in range(1,len(lst)):
        new_node={
            "data":lst[i],
            "link":None
        }
        tmp["link"]=new_node
        tmp=new_node
    return ll
    

    

lst=[10,20,30,40,50]
linked_list(lst)