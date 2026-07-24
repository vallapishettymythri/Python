#swapping of 2 numbers using bitwise
a=int(input("a:"))
b=int(input("b:"))
a=a^b
b=a^b
a=a^b
print("a:", a)
print("b:", b)
