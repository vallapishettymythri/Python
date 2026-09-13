#WAP to check a passowrd is valid or invalid
#atleast 8 characters
#contains atleast one upper case
#atleast one number
import re
string="Mythri12"
pattern="[a-zA-Z0-9]{8}"
re.findall(pattern,string)