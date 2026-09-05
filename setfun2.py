#remove()
s={2,3,4,5,6,7,1000,80,90}
s.remove(1000)
s

#using function
def my_remove(s,element):
    res=[]
    for i in s:
        if i!=element:
            res.append(i)
    return res

s={2,3,4,5,6,7,1000,80,90}
element=1000
my_remove(s,1000)


#discard()
s={2,3,4,5,6,7,1000,80,90}
s.discard(1000)
s
s.discard(1000) #no error even the value is discarded

#discard using function
def my_discard(s,element):
    res=[]
    if element not in s:
        return 
    else:
        for i in s:
            if i!=element:
                res.append(i)
    return set(res)
s={2,3,4,5,6,7,80,90}
my_discard(s,1000)