#[]- meta characters- matches a or b.
import re
string="bababa"
pattern="[ab]"
print(re.match(pattern,string))

#match()-It will see the starting only

#findall()- it will return all string where the pattern is matching
#findall()
import re
string="abababa"
pattern="[ab]"
print(re.findall(pattern,string))


#findall()
import re
string="abababa"
pattern="[ab]+"
print(re.findall(pattern,string))


string="python is simple language and Python is vast"
pattern="python|Python"
print(re.findall(pattern,string))


string="I have 12 apples and 20 books"
pattern="[0-9]+"
print(re.findall(pattern,string))