#a for loop is used to iterating over a sequence. As we say we can iterate in list, tuple, set and dictionaries.
#range()- returns sequence of numbers starting from 0 by default
for x in range(6):
    print(x)


for x in range(2,6):
    print(x)  #starts from 2.. but doesnt prints 6


for x in range(2,30,3):
    print(x)  #increaments the values by 3

#Break, continue and else is same in here as while loop. The functionality doesnt change the only change here is for loop and its condition.


#nested loops-
adj=["red","big","tasty"]
fruits=["apple","banana","cherry"]
for x in adj:
    for y in fruits:
        print(x,y)

#pass statement is used same has if else. When there is no value to prevent error we use pass. 