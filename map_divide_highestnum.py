#WAP to divide the each number by the highest value present in the value
def highestvalue(x):
    high=max(lst)
    return x/high
lst=[4,5,6,7,19,20]
list(map(highestvalue,lst))