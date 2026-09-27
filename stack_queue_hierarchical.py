#implementation of data structure, stack,queue.
class dataStructure:
    def __init__(self):
        self.data=[]
class stack(dataStructure):
    def push(self,element):
        self.data.append(element)
        return self.data
    def pop(self):
        self.data.pop(-1)
        return self.data
class queue(dataStructure):
    def enqueue(self,element):
        self.data.append(element)
        return self.data
    def dequeue(self):
        self.data.pop(0)
        return self.data
