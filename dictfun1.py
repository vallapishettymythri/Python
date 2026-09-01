dict={
    1:200,1:300,5:400,5:700
}
#keys()
dict.keys()


#values()
dict.values()

#popitem():
dict.popitem()



#pop_item() using func
def my_popitem(dict):
    value=0
    for key in dict:
        value=key
    key1,value1=value,dict[value]
    del dict[value]
    return key1,value1
dict={
    2:100,
    5:600,
    7:800,
    10:1000,
    11:45
}
my_popitem(dict)