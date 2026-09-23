#Implement a stack -push,pop,peep
class stack_implementation:
    def __init__(self):
        self.stack=[]
    def push(self,element):
        self.stack.append(element)
        return self.stack
    def pop(self):
        if self.isempty():
            return "Stack is empty we cannot pop"
        else:
            self.stack.pop(-1)
            return self.stack
    def isempty(self):
        if len(self.stack)==0:
            return True
        else:
            return False
    def peep(self):
        return self.stack[-1],self.stack
s=stack_implementation()
s.push(10)
s.push(20)
s.push(30)
s.pop()
s.peep()