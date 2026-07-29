#we need to check wehther a kth bit of a number is set or not from right.
a=int(input("a:"))
key=int(input("key:"))
if (a>>key)&1==1:
    print("True")
else:
    print("False")


#kth bit of a number os set or not from left
if(a&(1<<key))!=0:
    print("True")
else:
    print("False")