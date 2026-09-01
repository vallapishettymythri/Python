#Two sum
def two_sum(lst):
    small={}
    for i in range(len(lst)):
        small[lst[i]]=i
    for i in range (len(lst)):
        value=target-lst[i]
        if value in small:
            return (i,small[value])
    
lst=[2,7,11,15]
target=9
two_sum(lst)