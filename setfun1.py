#Empty set
s=set()
type(s)
#we cant access the elements in the set as we do for other.

#Iterative
s={2,3,4,5}
for i in s:
    print(i)


#add()
s={2,3,4,5}
s.add(1000)
print(s)

#add using function.
def my_add(s,element):
    lst=list(s)
    lst.append(element)
    return set(lst)
s={2,3,4,5,6,7}
my_add(s,2000)




#update()
s={2,3,4,5,6,7}
s.update([45,67,90])
s


#update using func
def my_update(s,lst):
    lst1=list(s)
    result=lst1+lst
    return set(result)

s={2,3,4,5,6,7}
lst=[1000,2000,3000]
my_update(s,lst)
