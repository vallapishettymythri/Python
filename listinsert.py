#Insert function- used to insert element in a given position
lst1 = [4, 5, 6, 7, 8, 9]
lst1.insert(2,3)
lst1


#Insert a number in a specific position without using insert
def  my_insert(lst,index,element):
    new_lst=[0]*(len(lst)+1)
    for i in range(index):
        new_lst[i]=lst[i]
    new_lst[index]=element
    for i in range(index,len(lst)):
        new_lst[i+1]=lst[i]
    return new_lst
    
lst = [3,4,5,6,7,8,9]
index=3
element=1000
my_insert(lst,index,element)