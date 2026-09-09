#replace()
s="16GB"
s.replace("GB","")


#alphabets--> #
#special symbol---> *
#numbers--->_
def convert(string):
    res=""
    for i in string:
        if i.isdigit():
            res+=i.replace(i,"_") #or-> res+="_"
        elif i.isalpha():
            res+=i.replace(i,"#") #or-> res+="#"
        else:
            res+=i.replace(i,"*") #or-> res+="*"

    return res
string="mythri@!$$12345"
convert(string)