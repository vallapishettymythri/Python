#WAP to count the number of words in a file
f1=open("myfile.txt","r")
data=f1.read()
words=data.split()
count=0
for i in words: #or print(len(lst))
    count+=1
print(count)
f1.close()