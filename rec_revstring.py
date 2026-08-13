#Reverse a string using recursion
def string(s):
    if s=="":
        return ""
    else:
        return string(s[1:])+s[0]
s=input("s:")
string(s)