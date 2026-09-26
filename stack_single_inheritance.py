class stack:
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
class child_stack(stack):
    def peep(self):
        return self.stack[-1],self.stack
obj=child_stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.pop()
obj.peep()
obj.isempty()