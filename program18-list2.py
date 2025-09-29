#change item in the list
thislist=["apple","banana","orange","cherry","kiwi","melon","mango"]
thislist[1]="pulm"
print(thislist)

thislist[1:3]="guava","berry"
print(thislist)

#insert items into the list
thislist.insert(2,"dragon")  #here 2 is the index where we want to insert the element.
print(thislist)