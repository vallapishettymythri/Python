#search()-search a particular pattern and returns
import re
string="abababa"
pattern="aba"
print(re.search(pattern,string))



#Groups-used for masking like # or even for not visibility
import re
string="mayurkulkarni5657@gmail.com"
pattern="([a-z0-9]+)(\@)([a-z]+)"
match=re.search(pattern,string)
match.group(1)



string="7777-8888-9999"
pattern="([0-9])([0-9]+)(\-)([0-9]+)(\-)(\d{3})(\d)" #{3} is quantifier
match=re.search(pattern,string) 
match.group(1)+len(match.group(2))*"#"+match.group(3)+len(match.group(4))*"#"+match.group(5)+len(match.group(6))*"#"+match.group(7)