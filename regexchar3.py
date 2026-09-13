#|- a or b..a|b


#\d- matches digit with string
#'\d'
import re
string="juleus ceaser died in 20 oct 1945"
pattern="\d"
print(re.findall(pattern,string))


string="juleus ceaser died in 20 oct 1945"
pattern="\d+"
print(re.findall(pattern,string))



#\w-matches alpha numeric
import re
string="abcdefg89765"
pattern="\w"
print(re.findall(pattern,string))



#'\W'-matches everything apart from the alphanumeric
string="abcdefg89765@#$%"
pattern="\W+"
print(re.findall(pattern,string))

