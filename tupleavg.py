#WAP to find the average elements of tuple
def avg(t):
    sum=0
    average=0
    for i in t:
        sum+=i
    average=sum/len(t)
    return average
t=(2,3,4,5,6,7)
avg(t)