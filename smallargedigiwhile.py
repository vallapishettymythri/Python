#find smallest and largest digit in the number using while loop
n=int(input("enter values:"))
small=large=n%10
while n>0:
    digit=n%10
    if(digit>large):
        large=digit
    if digit < small:
        small=digit
    n//=10
print(large,small)
    
