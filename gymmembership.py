#gym membership fee calculator
plan = input()
years = int(input())

if plan == "Basic":
    monthly = 500
elif plan == "Premium":
    monthly = 1000

amount = monthly * 12 * years

if years > 1:
    amount = amount * 85 // 100

print("Fee: ₹" + str(amount))
