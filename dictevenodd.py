#Print even and odd in dictionary and list inside dictionary
def evenodd(lst):
    result={
        "even":[],
        "odd":[]
    }
    for i in lst:
        if i%2==0:
            result["even"].append(i)
        else:
            result["odd"].append(i)
        
    return result
lst=[2,3,4,5,6,7,8,10,16,19]
evenodd(lst)