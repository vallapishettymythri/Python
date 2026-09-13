#Extract # words
import re
string="I love #python,#ML and #AI"
pattern="#\w+"
print(re.findall(pattern,string))