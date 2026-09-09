#WAP to find the minimum and maximum length of the word
def minmax(string):
    lst=string.split()
    maxi=mini=lst[0]
    for i in range (len(lst)):
        if len(lst[i])>len(maxi):
            maxi=lst[i]
    for i in range (len(lst)):
        if len(lst[i])<len(mini):
            mini=lst[i]
    return maxi,mini
        
string="This is a Python programming" 
minmax(string)