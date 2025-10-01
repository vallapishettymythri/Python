#Unpacking- We normally assign value to a variable it is called "Packing". 
#We are also allowed to extract the values back into variables. This is called "Unpacking". 
x=("apple","banana","cherry")
(green,yellow,red)=x
print(green)
print(yellow)
print(red)


#Asterisk*-If number of variables is less than item, we can use asterisk to the variable 
#name and the values will be assigned!
y=("apple","banana","cherry","kiwi","dragon","guava")
(green,yellow,*red)=y
print(green)
print(yellow)
print(red)

#What if the aesterisk is on the middle not to end. And it will take the values leaving according to next variables.
y=("apple","banana","cherry","kiwi","dragon","guava")
(green,*yellow,red)=y
print(green)
print(yellow)
print(red)
