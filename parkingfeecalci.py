#Parking fee calculator
hours = int(input())
day = input()

if day == "Saturday" or day == "Sunday":
    fee = 100
elif hours <= 2:
    fee = 30
elif hours <= 5:
    fee = 30 + (hours - 2) * 20
else:
    fee = 30 + 3 * 20 + (hours - 5) * 10

print("Fee: ₹" + str(fee))