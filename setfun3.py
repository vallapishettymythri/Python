#Pop()-
s={2,3,4,5,6,7,80,90}
s.pop()


#copy()
s={2,3,4,5,6,7,80,90}
ss=s.copy()
ss

#copy using function
def my_copy(s):
    ss=[]
    for i in s:
        ss.append(i)
    return set(ss)
s={2,3,4,5,6,7,80,90}
my_copy(s)