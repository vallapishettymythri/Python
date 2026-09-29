#sum of even numbers
from functools import reduce
lst=[2,3,4,5,6,7]
def even(x):
    return x%2==0
def fun2(x,y):
    return x+y
result=list(filter(even,lst))
reduce(fun2,result)