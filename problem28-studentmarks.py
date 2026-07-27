#Student Marks and Division Calculation
#Write a Python code to read the roll no, name and marks of three subjects and calculate the total, percentage and division.
rollno=int(input("Input the roll no of the student:"))
name=input("Input the name of the student:")
phy = int(input("Physics Marks: "))
chem = int(input("Chemistry Marks: "))
comp = int(input("Computer Marks: "))
print("Roll No:",rollno)
print("Name of Student:",name)
print("Marks in Physics:",phy)
print("Marks in chemistry:",chem)
print("Marks in computer application:",comp)
total=phy+chem+comp
print("Total Marks:",total)
percentage=total/3

print("Percentage:",percentage)
if percentage >=75:
    division="First"
elif percentage >=50:
    division="Second"
elif percentage <=50:
    division="Third"
print("Division:", division)