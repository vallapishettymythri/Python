#Car Rental Charge Calculator
# Write your code here

car_type = input()
day = input()

if car_type == "Sedan":
    cost = 1000
elif car_type == "SUV":
    cost = 1500

if day == "Saturday" or day == "Sunday":
    cost = cost + (cost * 20 // 100)

print("Cost: ₹" + str(cost))