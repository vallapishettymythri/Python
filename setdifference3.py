#wap to find set difference of 3 sets
def diff(s1,s2,s3):
    ss=set()
    for i in s1:
        if i not in s2 and s3:
            ss.add(i)
    return ss
s1={4,5,6,7,8,9}
s2={7,8,9,10,11}
s3={9,10,11}
diff(s1,s2,s3)