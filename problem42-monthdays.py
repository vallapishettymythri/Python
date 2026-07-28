# days in a month
month=int(input("Month number:"))
if month in [1,3,5,7,8,10,12]:
    print("Months has 31 days")
elif month==2:
    print("It has 28 or 29 days")
else:
    print("Has 30 days")