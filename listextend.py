#extend function()- used to merge two list
lst1=[4,5,6,7,8,9]
lst2=[10,15,17,18]
lst1.extend(lst2)
lst1


#Using while loop and append to extend
def extendser(lst1, lst2):
    res = []
    i = 0
    while i < len(lst1):
        res.append(lst1[i])
        i += 1
    j = 0
    while j < len(lst2):
        res.append(lst2[j])
        j += 1
    return res
    
lst1=[4,5,6,7,8,9]
lst2=[10,15,17,18]
extendser(lst1,lst2)




#using append to extend
def merging(lst1, lst2):
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


lst1 = [4, 5, 6, 7, 8, 9]
lst2 = [10, 15, 17, 18]

merging(lst1, lst2)