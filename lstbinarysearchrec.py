#Using recursion O(log n)
def binary(lst,low,high,key):
    if low>high:
        return False
    mid=(low+high)//2
    if lst[mid]==key:
        return True
    elif key>lst[mid]:
        return binary(lst,mid+1,high,key)
    else:
        return binary(lst,low,mid-1,key)
lst=[1,2,4,5,8]
key=int(input("key:"))
binary(lst,0,len(lst)-1,key)
        