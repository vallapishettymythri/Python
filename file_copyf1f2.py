#WAP to copy the content of f1 to f2.
f1=open("file1.txt","w")
f1.write("this is a content of file1\n")
f1.write("copy the content of file1 to file2")
f1.close()

f1=open("file1.txt","r")
f2=open("file2.txt","w")
data=f1.read()
f2.write(data)
f2.close()

f2=open("file2.txt","r")
print(f2.read())
f2.close()