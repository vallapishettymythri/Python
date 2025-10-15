#There are two primitive loops 1)While 2)For
#1)While loop use can execute a set of statements as long as condition is true.
i=1
while i<6:
    print(i)
    i+=1

#2)Break stmt can stop the loop if condition is true.
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1

#3)continue can stop current iteration and continue with next
i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)

#4)Else 
i=1
while i<6:
    print(i)
    i+=1
else:
    print("i is not less than 6")