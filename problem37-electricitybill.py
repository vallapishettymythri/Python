#Electricity Bill Calculation
#Write a program in Python to calculate and print the electricity bill of a given
#customer. The customer ID, name, and unit consumed by the user should be
#captured from the keyboard to display the total amount to be paid to the
cusid=int(input("id:"))
name=(input("name:"))
unit=int(input("unit:"))

print("Customer IDNO:",cusid)
print("Customer name:",name)
print("Unit consumed:",unit)
amount=0

if unit<=199:
    amount=unit*1.20
elif unit>200 and unit<400:
    amount=unit*1.50
elif unit>=400 and unit<600:
    amount=unit*1.80
else:
    amount=unit*2.00
if amount > 400:
    surcharge=amount*(15/100)
    amount+=surcharge
if amount < 100:
    amount=100
print("amount charges", amount)
print("Surchage amount", surcharge)
