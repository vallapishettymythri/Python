#wap to find minimum and maximum value in the dictionary
def minimax(dict):
    min=max=dict[1]
    for key in dict:
        if max<dict[key]:
            max=dict[key]
        elif min>dict[key]:
            min=dict[key]
    return min,max
dict={1:200,3:1000,5:1300,8:900}
minimax(dict)