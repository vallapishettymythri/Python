# Simple Calculation

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
choose = int(input("Enter your choice (1-4): "))

if choose == 1:
    print("The Addition:", a + b)
elif choose == 2:
    print("The Subtraction:", a - b)
elif choose == 3:
    print("The Multiplication:", a * b)
elif choose == 4:
    print("The Division:", a / b)
else:
    print("Invalid Choice")