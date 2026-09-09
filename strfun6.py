#Sorted():
string="xanbp"
sorted(string)

#Using function
def sort(string):
    lst=list(string)
    for i in range (len(lst)):
        for j in range(i+1,len(lst)):
            if ord(lst[i])>ord(lst[j]):
                lst[i],lst[j]=lst[j],lst[i]
                
                
    return lst
string="xanbp"
sort(string)


#reversed()- gives adress
string="xanbp"
reversed(string)


#reverse()-type cast to get exact answer
string="xanbp"
list(reversed(string))



#Reversed using fun
def reverse(string):
    lst=list(string)
    i=0
    j=len(lst)-1
    while i<j:
        lst[i],lst[j]=lst[j],lst[i]
        i+=1
        j-=1
    return lst
string="xanbp"
reverse(string)