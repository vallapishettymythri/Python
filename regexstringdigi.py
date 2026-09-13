#WAP to check whether a string contains all digits or not
import re
def digits(string):
    pattern="\d+"
    match = re.fullmatch(pattern, string)
    if match:
        return True
    else:
        return False
string="123456789g"
digits(string)