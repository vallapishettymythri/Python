#superset()
s1={1,2,3,4,5,6}
s2={5,6}
s1.issuperset(s2)


s2.issuperset(s1)

def my_superset(s1,s2):
    for i in s2:
        if i not in s1 :
            if s1<s2:
                return False
    return True
s1={1,2,3,4,5,6}
s2={5,6}
my_superset(s2,s1)