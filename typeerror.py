#wap to handle the exception for type error
try:
    a=int(input("a:"))
    print(lst[a])
except:
    print("type error")