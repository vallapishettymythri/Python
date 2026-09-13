#sub-is used to replace parts of a string.
import re
st1="i have 12 apples and 7 oranges"
pattern="\d"
print(re.sub(pattern,"#",st1))


#\b-boundary
st3="cat catlong babycat"
pattern=r"\bcat\b"
print(re.findall(pattern,st3))


