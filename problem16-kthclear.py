#WAP to kth bit clear or not
a=int(input("Enter a:"))
k=int(input("k:"))
a&=~(1<<k)
print(a)
#to make a certain kth bit has zero. 