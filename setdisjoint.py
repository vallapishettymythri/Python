#Disjoint()
s1={1,2,3}
s2={3,4,5}
s1.isdisjoint(s2) #no elements should be common


def my_disjoint(s1,s2):
    for i in s1:
        if i in s2:
            return False
    return True
s1={1,2,3}
s2={4,5}
my_disjoint(s1,s2)