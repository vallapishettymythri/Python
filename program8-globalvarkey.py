#there is a seperate keyword too for mention the global variable. It is "global".
def myfunc():
    global x
    x="fantastic"
myfunc()
print("Python is " +x)