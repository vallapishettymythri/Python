#binary search
#using function
def binary(lst,key):
    low=0
    high=len(lst)-1
    for i in range (len(lst)): #while low<=high:
        mid=(low+high)//2
        if lst[mid]==key:
            return "True"
        elif key>lst[mid]:
            low=mid+1
        else:
            high=mid-1
    return False
lst=[1,2,4,5,8]
key=int(input("key:"))
binary(lst,key)
        