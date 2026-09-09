#Upper()
st1="mayur"
res=st1.upper()
res


#Using function for upper
def my_upper(string):
    res=""
    for i in string:
        var=ord(i)-32
        res+=(chr(var))
    return res
string="mayur"
my_upper(string)


#Lower()-
st1="MAYUR"
res=st1.lower()
res