#WAP to extract 5 length character word
import re
string="python is fun and great"
pattern=r"\b\w{5}\b"
print(re.findall(pattern,string))