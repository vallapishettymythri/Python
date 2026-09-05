#subset
s1={1,2,3,4,5,6,}
s2={5,6}
s1.issubset(s2) #false
s2.issubset(s1) #true

#using function
def my_subset(s1,s2):
    for i in s2:
        if i not in s1:
                return True
    return False
s1={1,2,3,4,5,6}
s2={5,6}
my_subset(s1,s2)