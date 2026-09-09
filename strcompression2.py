#String compression (Variation 2)- Try
def compression(s):
    s1=s[0]
    count=1
    for i in range(1,len(s)):
        curr=s[i]
        prev=s[i-1]
        if curr==prev:
            count+=1
        else:
            if count%2==0:
                s1+=str(count)
                s1+=curr
                count=1
            elif count%2!=0:
                s1+=s[i]
                count=1
                
    return s1
s="aabbbccccdddeeeef"
compression(s)