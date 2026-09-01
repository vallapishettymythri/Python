#pop()- it returns and deletes the value
def my_pop(d,key):
    result={}
    value=d[key]
    for k in d:
        if k!=key:
            result[k]=d[k]
    return value,result

d={
    2:300,
    5:700,
    8:900,
    10:1000
}
key=8
my_pop(d,key)

#copy():
dict1={
    2:300,
    5:700,
    8:900,
    10:1000
}
dict2={}
dict2= dict1.copy()
dict2



#update():
dict3={
    "name":"abc",
    "city":"Hyderabad"
}
dict3.update({"marks":75,"grade":"A"})
dict3



def my_update(dict1,update_items):
    result={}
    for i in dict1:
        result[i]=dict1[i]
    for i in update_items:
        result[i]=update_items[i]
    return result

dict1={
    "name":"abc",
    "city":"Hyderabad"
}
update_items={"marks":75,"grade":"A"}
my_update(dict1,update_items)