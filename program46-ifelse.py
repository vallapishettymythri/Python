#Python supports usual logical conditions. 
#1) If statement
a=33
b=200
if b>a:
    print("b is great") #need to have indentation.

#2)if-else
a=200
b=33
if b>a:
    print("b is great")
else:
    print("a is great")


#3)elif- if previous condition isnt true then try this condition.
a=33
b=33
if b>a:
    print("b is great")
elif a==b:
    print("a and b are same")


#4)Else: Catches anything which isnt caught by the preceding conditions
a=200
b=33
if b>a:
    print("b is great")
elif a==b:
    print("a and b are same")
else:
    print("a is greater than b")


#5)Nexted if
x=15
if x>10:
    print("Above ten")
    if x>20:
        print("and above 20")
    else:
        print("not above 20")

#6)Pass- If stmts can't be empty. If stmt has no content then put pass to avoid error.
a=33
b=200
if b>a:
    pass


