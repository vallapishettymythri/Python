#wap to give all possible substrings
def sub(string):
    i=0
    for i in range (len(string)):
        for j in  range (i+1,len(string)):
            print(string[i:j])
            
string="ababa"
sub(string)