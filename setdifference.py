#difference()
s1={3,4,5,6,7,8,9}
s2={7,8,9,10}
s1.difference(s2) #element present in s1 not present in s2.

#using function
def diff(s1,s2):
    ss=set()
    for i in s1:
        if i not in s2:
            ss.add(i)
    return ss
s1={3,4,5,6,7,8,9}
s2={7,8,9,10}
diff(s1,s2)