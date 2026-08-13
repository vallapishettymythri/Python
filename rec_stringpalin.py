#Wap to print string is palindrome(1st)
def string(s):
    if len(s)<=1:
        return True
    if s[0]!=s[-1]:
        return False
    return string(s[1:-1])
    
s=input("s:")
string(s)