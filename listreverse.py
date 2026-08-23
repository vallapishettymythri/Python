#Reverse a list
def reverse_lst(lst):
    i=0
    j=len(lst)-1
    while i < j:
        lst[i],lst[j]=lst[j],lst[i]
        i+=1
        j-=1
    return lst
lst = [3,4,5,6,7,8,9]
reverse_lst(lst)