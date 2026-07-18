#Bitwise operator-
#Works on each and every Bit.

#&   bitwise and
#|   bitwise or 
#^   xor
#>>  right shift
#<<  left shift
#~   complement

print(2 & 3) #this works has the logical and. 
#2- 0   0 0 1 0
#3- 0   0 0 1 1
#   0   0 0 1 0 - output is 2. the first bits shows whether the number is negative or positive.
print(-13 & -15)

print(11|6)
#11- 0  1 0 1 1
#6-  0  0 1 1 0
#    0  1 1 1 1
print(-15|9)


print(19^-9)
print(-6^-15)


print(~5)
print(~6)
print(~(~8))
print(~-7)


print(80>>4) #we divide the number and remainder by 4 times by 2.
print(10<<4) #we multiply the number and its remainder by 4 times by 2. 

print(3^3^~8>>1<<2)