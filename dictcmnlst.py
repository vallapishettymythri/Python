#WAP to find the common elements between the list
def common(lst1,lst2):
    small={}
    result=[]
    for i in lst2:
        small[i]=1
    for i in lst1:
        if i in small:
            result.append(i)
    return result
            
            
lst1=[3,4,5,6,7]
lst2=[6,7,8,9]
common(lst1,lst2)