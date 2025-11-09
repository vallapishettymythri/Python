#Python doesn't support arrays but python lists can be used.
# #It is same like list. To use the arrays we need to import numpy which we will learn soon.
#An array is a special variable which can hold more than one value at a time.
cars = ["Baleno", "MG", "Benz"]
x = cars[0]  # access
print(x)

cars1 = ["Baleno", "MG", "Benz"]
cars1[0] = "Toyota"  # modify
print("After modification:", cars1)

x = len(cars1)  # length of array
print("Length:", x)

for car in cars1:     # loop through each element
    print(car)

cars1.append("Honda")  # adding element
print("After adding:", cars1)

cars1.pop(1)  # remove element at index 1
print("After removing index 1:", cars1)