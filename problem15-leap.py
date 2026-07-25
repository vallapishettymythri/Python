#WAP to check whether a particular number is a leap year or not.
yr=int(input("Enter the year:"))
if  yr%4==0 and yr%100!=0 or yr%400==0:
    print("Leap year")
else:
    print("Not leap year")