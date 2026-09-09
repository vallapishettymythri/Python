#join()
lst=["python","is","a","programming","language"]
result=" ".join(lst)
result


#join using fun
def  my_join(lst):
    result=lst[0]
    for i in range (1,len(lst)):
        result+=" "+str(lst[i])
    return result
lst=["python","is","a","programming","language"]
my_join(lst)


#Startswith()
string="python is a programming language"
string.startswith("py")


#using func
def my_start(string,letter):
    for i in range (len(letter)):
        if string[i]!=letter[i]:
            return False
    return True
string="python is a programming language"
letter="py"
my_start(string,letter)


#endswith()
string="python is a programming language"
string.endswith("uage")


#capitalize
string="python is a programming language"
string.capitalize()


#Title()
string="python is a programming language"
string.title()