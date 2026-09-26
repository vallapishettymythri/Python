class queue:
    def __init__(self):
        self.stack=[]
    def enqueue(self,element):
        self.stack.append(element)
        return self.stack
    def dequeue(self):
        if self.isempty():
            return "Stack is empty we cannot pop"
        else:
            self.stack.pop(0)
            return self.stack
    def isempty(self):
        if len(self.stack)==0:
            return True
        else:
            return False
class using_queue(queue):
    def __init__(self):
        super().__init__()
    def display(self):
        print(self.stack)
qq=using_queue()
qq.enqueue(20)
qq.enqueue(30)
qq.dequeue()
qq.display()
qq.isempty()
        