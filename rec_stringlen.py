#Wap to print string length
def string(s):
    if s=="":
        return 0
    else:
        return 1+string(s[1:])
s=input("s:")
string(s)