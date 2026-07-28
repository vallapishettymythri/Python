#Day Number to Day Name
#Write a Python code to read any day number in integer and display the day
#name in word format.
no=int(input("Enter day number:"))
if no==1:
    print("Monday")
elif no==2:
    print("Tuesday")
elif no==3:
    print("Wednesday")
elif no==4:
    print("Thursday")
elif no==5:
    print("Friday")
elif no==6:
    print("Saturday")
elif no==7:
    print("Sunday")
else:
    print("Unknown")
    