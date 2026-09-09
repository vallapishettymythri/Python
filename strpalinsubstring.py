#WAP to give palindrome substrings
def is_palin(string):
    for i in range(len(string)):
        for j in range(i+1,len(string)):
            s=string[i:j]
            if palin(s):
                print(s)
def palin(string):
    i=0
    j=len(string)-1
    while i<=j:
        if string[i]!=string[j]:
            return False
        i+=1
        j-=1
    return True
string="ababababa"
is_palin(string)