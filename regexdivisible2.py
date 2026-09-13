#WAP to extract all the words whose length is divisible by 2
import re
string="this is python programmingg language"
pattern=r"\b[a-z]{2}\b|\b[a-z]{4}\b|\b[a-z]{6}\b|\b[a-z]{8}\b|\b[a-z]{10}\b|\b[a-z]{12}\b"
print(re.findall(pattern,string))



string="this is python programmingg language"
result=[]
res=re.findall("\w+",string)
for i in range(len(res)):
    if len(res[i])%2==0:
        result.append(res[i])
print(result)
        
