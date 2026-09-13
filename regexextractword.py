#Extract word
import re
string="<HTML><HEAD><TITLE>welCoMe</TITLE></HEAD></HTML>"
pattern=r"[a-zA-Z]+"
print(re.findall(pattern,string))