#tuples are heterogeneous
t1=(23,67,8,"abc",True)
t1


#Accessing
t2=(45,67,89,90,99,12)
t2[5]

t2[2:6]




#coversion
t=(45,67,89,90,99,12)
lst1=list(t)
print(lst1)
lst1[3]=100
print(lst1)
print(tuple(lst1))