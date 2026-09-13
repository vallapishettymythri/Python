#wap to extract that word which is repeating
import re
string="Hello Hello this is python"
pattern=r"\b(\w+)\s+\1\b"
print(re.findall(pattern,string))