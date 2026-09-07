moisture = int(input())
weather = input()

if weather == "Sunny" and moisture < 50:
    print("Water now")
elif moisture < 30:
    print("Water now")
elif moisture <= 60:
    print("Check tomorrow")
else:
    print("No water needed")