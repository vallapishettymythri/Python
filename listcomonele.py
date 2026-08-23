#WAP to find the common elements between 2 lists and also give the count of common elements
#using func
def common(lst1,lst2):
    result=[]
    count=0
    for i in lst1:
        for j in lst2:
            if i==j:
                count+=1
                result.append(i)
    return result,count
lst1=[3,4,5,6,7,8,9]
lst2=[7,8,9,10,15]
common(lst1,lst2)



#WAP to find the common elements between 2 lists and also give the count of common elements
def common(lst1,lst2,i,j,count):
    if i==len(lst1):
        return count
    if j==len(lst2):
        return common(lst1,lst2,i+1,0,count)
    if lst1[i]==lst2[j]:
        count+=1
        return common(lst1,lst2,i+1,0,count)
    else:
        return common(lst1,lst2,i,j+1,count)

lst1=[3,4,5,6,7,8,9]
lst2=[7,8,9,10,15]
common(lst1,lst2,0,0,0)