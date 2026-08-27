#Bubble sort
def bubble(lst):
    for i in range (len(lst)-1):
        for j in range(len(lst)-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
lst=[5,1,4,2,8]
bubble(lst)
    