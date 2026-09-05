#symmetric_difference()
s1={3,4,5,6,7,8,9}
s2={7,8,9,10}
s1.symmetric_difference(s2)


#using function
def sym(s1,s2):
    ss=set()
    for i in s1:
        if i not in s2:
            ss.add(i)
    for j in s2:
        if j not in s1:
            ss.add(j)
    return ss
s1={3,4,5,6,7,8,9}
s2={7,8,9,10}
sym(s1,s2)