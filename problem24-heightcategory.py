#Height Categorization
#Write a Python code to accept the height of a person in centimeters and
#categorize the person according to their height.
h=int(input("Enter height:"))
if h<150:
    print("The person is dwarf")
elif h>180:
    print("the person is tall")
else:
    print("the person is average height")