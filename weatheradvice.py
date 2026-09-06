n = int(input())
s = input()

if n > 30:
    weather = "Hot"
elif n < 10:
    weather = "Cold"
else:
    weather = "Moderate"

if s == "True":
    print(weather + ". Carry umbrella.")
else:
    print(weather)