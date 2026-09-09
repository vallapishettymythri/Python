#min()
string="abc"
min(string)

#max()
string="abc"
max(string)


#Using loop
def minmax(string):
    minele=maxele=string[0]
    for i in range(1,len(string)):
        if ord(maxele)<ord(string[i]):
            maxele=string[i]
        if ord(minele)>ord(string[i]):
            minele=string[i]
    return minele,maxele
string="abc"
minmax(string)