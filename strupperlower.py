#Upper to lower and lower to upper
def change(string):
    res=""
    for i in string:
        if ord(i)>=65 and ord(i)<97 : #to lower case
            var=ord(i)+32
            res+=(chr(var))
        else:
            var=ord(i)-32
            res+=(chr(var))
    return res


string="MaYuR"  
change(string)