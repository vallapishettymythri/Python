#WAP to toggle kth bit. 
a=int(input("a:"))
k=int(input("k:"))
a^=(1<<k)
print(a)

#7-> binary form is 
#0 1 1 1 k=2 means toggle the 1 to 0 if there is 0 then 0 to 1.
#we will be doing left shift of the 1 in binary form of k which is 2.
#so 0 1 0 0
#0 1 1 1
#0 1 0 0 we will peform xor 
#0 0 1 1 the second bit is toggled from 1 to zero by forming a new number 3 as output.
