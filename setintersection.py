#intersection()
s1={3,4,5,6,7,8,9}
s2={7,8,9,10}
s1.intersection(s2)


#intersection using function
def inter(s1,s2):
    ss=set()
    for i in s1:
        for j in s2:
            if i==j:
               ss.add(i)
    return ss
s1={3,4,5,6,7,8,9}
s2={7,8,9,10}
inter(s1,s2)