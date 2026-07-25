#Admission Eligibility Check
#Write a Python code to determine eligibility for admission to a professional
#course based on the following criteria:
math=int(input("Enter maths marks:"))
phy=int(input("Enter physics marks:"))
chem=int(input("Enter chemistry marks:"))
total=math+phy+chem
mathphy=math+phy
print("Total:",total)
print("Maths and physics:",mathphy)
if (math>=65 and phy>=55 and chem>=50 and (total >=90 or mathphy>=140)):
    print("The candidate is not eligible for admission.")
else:
    print("The candidate is not eligible for admission.")