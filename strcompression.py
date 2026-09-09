#String compression
def compression(s):
    s1=s[0]
    count=1
    for i in range (1,len(s)):
        curr=s[i]
        prev=s[i-1]
        if curr==prev:
            count+=1
        else:
            if count>1:
                s1+=str(count)
                count=1
            s1+=curr
    return s1
        
s="aaabbcccdeeef"
compression(s)