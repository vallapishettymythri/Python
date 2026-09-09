#Battery Status Checker
# Write your code here
battery = int(input())
charging = input()

if battery < 20:
    print("Power saving mode ON")

if charging == "True":
    print("Fast charging")
else:
    print("slow")
