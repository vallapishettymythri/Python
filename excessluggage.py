travel_class = input()
weight = int(input())

if travel_class == "Economy":
    limit = 15
elif travel_class == "Business":
    limit = 30

if weight > limit:
    excess = weight - limit
    fee = excess * 500
    print("Excess Fee: ₹" + str(fee))
else:
    print("No Extra Fee")