# Temperature-Based Weather Message
#Write a Python code to read temperature in centigrade and display a suitable
#message according to the temperature state below:
temp=int(input("temp:"))
if temp<0:
    print("The freezing weather")
elif temp<10:
    print("Very cold weather")
elif temp<20:
    print("Cold weather")
elif temp<30:
    print("Normal in temp")
elif temp<40:
    print("its hot")
else:
    print("its very hot")
