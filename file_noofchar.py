#WAP to find the number of characters in the file
f1=open("myfile.txt","r")
data=f1.read() #strores the f1.read in the data which is string
count=0
for i in data:
    count+=1
print(count)
f1.close()