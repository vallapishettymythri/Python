#min max functions are directly used to find the mininum and maximum of a list.
#Min and max
def min_max(lst):
   return min(lst), max(lst)
lst=[3,4,5,100,7,8]
min_max(lst)


#Min max using loop
def min_max(lst):
    maxel=minel=lst[0]
    for i in range (len(lst)):
        if lst[i]>maxel:
            maxel=lst[i]
        if lst[i]<minel:
            minel=lst[i]
    return minel,maxel
lst=[3,4,5,100,7,8]
min_max(lst) 


#Divide and conquer for recurssion- If we have a problem p. P is larger problem then divide it into su problems.
#If subproblems itself is a large, again need to divide
#Continue divide until it becomes a small problem
#A small problem is which is getting solved in one or two approaches. 
#Using recursion(Divide and conquer stratergy)
def min_max(lst,low,high):
    if low==high:
        min_ele=max_ele=lst[low]
        return min_ele,max_ele
    elif high==low+1:
        if lst[low]>lst[high]:
            min_ele=lst[high]
            max_ele=lst[low]
        else:
            min_ele=lst[low]
            max_ele=lst[high]
        return min_ele, max_ele
    else:
        mid=(low+high)//2
        left_min,left_max=min_max(lst,low,mid)
        right_min,right_max=min_max(lst,mid+1,high)
        original_min=smaller(left_min,right_min)
        original_max=bigger(left_max,right_max)
        return original_min,original_max

def bigger(a,b):
    if a > b:
        return a
    else:
        return b 
def smaller(a,b):
    if a<b:
        return a
    else:
        return b

lst = [23,11,67,33,-45,-100,78,89,12,99,110]
minimum, maximum = min_max(lst, 0, len(lst) - 1)
print("Minimum:", minimum)
print("Maximum:", maximum)