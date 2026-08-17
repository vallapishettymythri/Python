#Len()- is a function to perform on the list. 
#It is a global func in python, it will return te length() of the list. 
#1.len() function
def my_length(lst):
    return len(lst)
lst=[3,4,5,100,7,8]
my_length(lst)

#len using loop
def my_length(lst):
    count=0
    for i in lst:
        count+=1
    return count
lst=[3,4,5,100,7,8]
my_length(lst)


#len using recursion
def my_length(lst):
    if lst==[]:
        return 0
    else:
        return 1+my_length(lst[1:])
lst=[3,4,5,100,7,8]
my_length(lst)  