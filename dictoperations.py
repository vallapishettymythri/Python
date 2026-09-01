#Mutable
dict={
    2:100,
    5:600,
    7:800,
    10:1000,
    11:45
}
dict[9]=9000
print(dict)


#No duplicates allowed
dict={
    1:200,1:300,5:400,5:700
}
dict


#Iterate
for key in dict:
    print(key)


for key,value in dict.items():
    print(key,value)


#keys()
dict.keys()


#values()
dict.values()