#WAP to find the difference of maximum and minimum element in the list
def differ(lst):
    maxima=minima=lst[0]
    for i in range (len(lst)):
        if lst[i]>maxima:
            maxima=lst[i]
        elif lst[i]<minima:
            minima=lst[i]
        difference=maxima-minima
    return difference
lst=[3,4,5,6,7,8,9]
differ(lst)