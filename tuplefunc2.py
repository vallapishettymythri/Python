#index()-
t=(34,12,5,6,7,8,90)
t.index(34)


#Usin loop
def my_index(t,element):
    for i in range(len(t)):
        if t[i]==element:
            return i
t=(34,12,5,6,7,8,90)
element=int(input("element:"))
my_index(t,element)



#count():
tt=(2,2,2,4,5,6,7,8,9,9,9,0)
tt.count(9)


#del()
del tt
tt



#Sorted()
tt=(34,11,-22,56,99,2,3,4,17)
tuple(sorted(tt))