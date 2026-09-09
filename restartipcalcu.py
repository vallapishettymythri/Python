bill = int(input())
service = input()

if bill > 5000:
    tip = bill * 15 // 100
elif bill > 2000:
    tip = bill * 10 // 100
else:
    tip = 0

if service == "Excellent":
    tip = tip + (bill * 5 // 100)

print("Tip: ₹" + str(tip))