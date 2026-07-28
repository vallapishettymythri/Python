#Profit and Loss Calculation
#Write a Python code to calculate profit and loss on a transaction.
sp=int(input("Selling price:"))
cp=int(input("Cost price:"))
if sp > cp:
    print("Profit")
elif cp>sp:
    print("Loss")
else:
    print("No profit, no loss")
    