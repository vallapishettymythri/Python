#WAP to check A indian mobile number is valud or not
import re
string="+918790289211"
pattern=r"\+91[6-9]\d{9}"
match=re.fullmatch(pattern,string)
if  match:
    print(True)
else:
    print(False)