#merge sort using recursion
def merge_sort(lst,low,high):
    if low>=high:
        return [lst[low]]
    else:
        mid=(low+high)//2
        left_lst=merge_sort(lst,low,mid)
        right_lst=merge_sort(lst,mid+1,high)
    return merge(left_lst,right_lst)


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


lst=[23,11,-22,56,12,67,-99,3]
low=0
high=len(lst)-1
merge_sort(lst,low,high)