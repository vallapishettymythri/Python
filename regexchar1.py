#1)"."-it will match a single character
#"."
import re
string="fan"
pattern="."
print(re.match(pattern,string))

#2)"*"- it will match zero or more characters
#"*"
import re
string="aaaaaa"
pattern="a*"
print(re.match(pattern,string))



#"*"
import re
string="bbbbb"
pattern="a*"
print(re.match(pattern,string))

#3)"+"- it will match one or more characters
#"+"
import re
string="aaa"
pattern="a+"
print(re.match(pattern,string))


#"+"
import re
string="bbb"
pattern="a+"
print(re.match(pattern,string))
#matches same has * but if there are no common it returns none unlike the *. It returns ''

