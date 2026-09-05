#WAP to get an Intersection of 3 sets
def inter(s1,s2,s3):
    ss=set()
    for i in s1:
        for j in s2:
            for k in s3:
                if i==j==k:
                    ss.add(i)      
    return ss
s1={4,5,6,7,8,9}
s2={7,8,9,10,11}
s3={9,10,11}
inter(s1,s2,s3)
