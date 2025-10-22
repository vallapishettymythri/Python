#args and kwargs are used when we need to pass a unknown number of arguments.(tuples)
#arbitary arguments-*args 
#It is used when we don't kniw how many arguments will be passed in to the function. We add * bfore parameter name.
def my_func(*kids):
    print("the youngest child is" +kids[2])
my_func("emily","thomas","linus")
