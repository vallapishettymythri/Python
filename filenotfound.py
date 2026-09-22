#wap to handle a filenotfound
try:
    f1.open("filenotfound.txt","r")
    f1.write()
    f1.close()
except:
    print("file not found")
    
    