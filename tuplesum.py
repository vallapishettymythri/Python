#Sum of nested tuple
def sum_tuple(tt):
    sum=0
    for i in tt:
        if type(i)==tuple:
            for j in i:
                sum+=j
        else:
            sum+=i
    return sum
tt=(3,4,5,6,7,(7,8,10))
sum_tuple(tt)