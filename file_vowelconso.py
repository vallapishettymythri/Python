#WAP to count the number of vowels and consonants in a file
f1=open("myfile.txt","r")
data=f1.read()
vowels=0
consonants=0
for i in data:
    if i in "aeiouAEIOU":
        vowels+=1
    else:
        consonants+=1
print(vowels,consonants)
f1.close()