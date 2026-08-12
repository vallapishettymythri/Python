# wap to find the multiplication of 2 no's using recursion
def recursive_mul(a,b):
    if b==0: #anchor 
        return 0
    else:
        return a+recursive_mul(a,(b-1)) #recursive
a=int(input("a:"))
b=int(input("b:"))
recursive_mul(a,b)