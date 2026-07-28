#WAP to check whether divisible by 10 and 5. (Nested if)
a=int(input("a:"))
if a%10==0:
    print("Divisible by 10")
    if a%5==0:
        print("Divisible by 5 and 10")
else:
    print("a is not divisible by 10")
    