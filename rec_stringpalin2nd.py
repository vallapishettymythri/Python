#Wap to print string is palindrome(2nd)
def string(s):
    if s=="":
        return ""
    else:
        return string(s[1:])+s[0]
s=input("s:")
reverse=string(s)
if reverse==s:
    print("true")
else:
    print("false")