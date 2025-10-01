#loop through a tuple
#1) For loop-
this=("apple","banana","cherry")
for x in this:
    print(x)

#2) Index- Range() and len()
for i in range(len(this)):
    print(this[i])

#3) While loop
i=0
while i<len(this):
    print(this[i])
    i=i+1