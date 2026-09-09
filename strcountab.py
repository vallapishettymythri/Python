#WAP to find the number of a's and number of b's
def num(string):
    acount=0
    bcount=0
    for i in string:
        if i=="a":
            acount+=1
        else:
            bcount+=1
    return acount,bcount
string="aaabbbaababbbaaa"
num(string)