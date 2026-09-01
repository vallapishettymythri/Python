#value key and ALternative add value
def alternative(lst):
    result={}
    for i in  range (len(lst)-1):
        result[lst[i]]=lst[i]+lst[i+1]
    return result
lst=[3,4,5,6,7,8,9,1]
alternative(lst)