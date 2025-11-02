#Lambda functions-small anonymous function. A lambda function take any number of
#arguments but can only have one expression.
x=lambda a:a+10
print(x(5)) #a=5

#multiple arguments
x=lambda a,b,c:a+b+c
print(x(2,3,4))

#inside a function
def myfunc(n):
    return lambda a:a*n
doubler=myfunc(2)
print(doubler(11))

#Lambda functions are even commonly used with built-in functions.
#map()- applies to every item
no=[1,2,3,4]
double=list(map(lambda x:x*2,no))
print(double)

#filter()-creates a list of itens for which a function returns true.
no=[1,2,3,4,5,6,7]
odd=list(filter(lambda x: x%2!=0,no))
print(odd)

#sorted()-sorts 
student=[("emil",24),("toba",22),("linus",23)]
sort=sorted(student,key=lambda x:x[1])
print(sort)