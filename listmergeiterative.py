# merge sort using iterative approach
def merge(lst1, lst2):
    i = j = 0
    result = []
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1
    if i == len(lst1):
        while j < len(lst2):
            result.append(lst2[j])
            j += 1
    if j == len(lst2):
        while i < len(lst1):
            result.append(lst1[i])
            i += 1
    return result

def mergesort(lst):
    size=1
    while size<len(lst):
        for i in range(0,len(lst),2*size):
            mid=i+size
            end=i+2*size
            if mid< len(lst):
                left=lst[i:mid]
                right=lst[mid:end]
                merged=merge(left,right)
                lst[i:end]=merged
        size*=2

    return lst
lst = list(map(int, input().split()))
mergesort(lst)