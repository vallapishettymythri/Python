#String without duplicates. Avoiding string repeatation (2-pointer approach)
def dupli(s):
    s1=s[0]
    for i in range(1,len(s)):
        curr=s[i]
        prev=s[i-1]
        if prev!=curr:
            s1+=curr
    return s1
        
s="aaabbcccdeeef"
dupli(s)