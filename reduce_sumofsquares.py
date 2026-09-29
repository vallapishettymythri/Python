#Sum of squares
from functools import reduce
lst=[2,3,4,5,6,7]
def fun1(x):
    return x**2
result=list(map(fun1,lst))
def fun2(x,y):
    return x+y
reduce(fun2,result)