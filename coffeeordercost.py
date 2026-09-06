coffee = input()
extra = input()

if coffee == "Espresso":
    amount = 50
elif coffee == "Latte":
    amount = 80
elif coffee == "Cappuccino":
    amount = 70

if extra == "True":
    amount += 20

print("Total: ₹" + str(amount))