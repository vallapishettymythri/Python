#loop lists
#1) for loop- prints all the items one by one
thislist=["apple","banana","cherry"]
for x in thislist:
    print(x)


#2)loop through index no: here, we use range() and len() to print one by one
for i in range(len(thislist)):
    print(thislist[i])


#3)while loop: use len() func to determine the length of the list. Start at 0 and loop your way through the list items by reffering indexes
i=0
while i< len(thislist):
    print(thislist[i])
    i=i+1