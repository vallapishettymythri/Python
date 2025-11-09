#Recursion: when a function calls itselfs.
#Simple Recursion:
def countdown(n):
    if n<=0:
        print("Done!")
    else:
        print(n)
        countdown(n-1) #calling countdown function it is recursion.

countdown(5)

#Every recursion has 2 parts. Base case:Condition that stops recursion.
#Recursion case: Function calling itself with a modified arguments.
#Factorial
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))


#Fibonacci
def fibbo(n):
    if n<=1:
        return n
    else:
        return fibbo(n-1) + fibbo(n-2)
print(fibbo(7))

#Recursion with lists
#1)Sum of the lists
def sum_list(numbers):
    if(len(numbers))==0:
        return 0
    else:
        return numbers[0]+sum_list(numbers[1:]) #this numbers[1:]-adds the sum of the list from 1 to all the elements.
mylist=[1,2,3,4,5]
print(sum_list(mylist))

#2)Maximum value
def find_max(no):
    if(len(no))==1:
        return no[0]
    else:
        maxno=find_max(no[1:])
        return no[0] if no[0] > maxno else maxno
mylist=[1,2,3,4,5]
print(find_max(mylist))