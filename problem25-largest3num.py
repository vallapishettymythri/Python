#Largest of Three Numbers
#Write a Python code to find the largest of three numbers.
n1=int(input("Enter num1:"))
n2=int(input("Enter num2:"))
n3=int(input("Enter num3:"))
print("1st Number =", n1, ", 2nd Number =", n2, ", 3rd Number =", n3)
if n1>n2 and n1>n3:
    print("The 1st Number is the greatest among three")
elif n2>n1 and n2>n3:
    print("The 2nd Number is the greatest among three")
else:
    print("The 3rd Number is the greatest among three")