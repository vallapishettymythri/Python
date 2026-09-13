#WAP to check a string ends with .com
import re
string="www.google.com"
match= re.findall("\.com",string)
if  match:
    print(True)
else:
    print(False)