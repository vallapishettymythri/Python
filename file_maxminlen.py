#WAP to find the maxmimum and minimum in file
f3=open("myfile.txt","r")
data=f3.read()
words=data.split()
maximum=words[0]
minimum=words[0]
for i in words:
    if len(i)>len(maximum):
        maximum=i
    if len(i)<len(minimum):
        minimum=i
print(maximum,minimum)
f3.close()