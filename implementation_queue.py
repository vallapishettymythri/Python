#Implementing queue- enqueue,dequeue,peep
class queue_implementation:
    def __init__(self):
        self.queue=[]

    def enqueue(self,element):
        self.queue.append(element)
        return self.queue
    def dequeue(self):
        if self.isempty():
            return "queue is empty we cannot pop"
        else:
            self.queue.pop(0)
            return self.queue
    def isempty(self):
        if len(self.queue)==0:
            return True
        else:
            return False
    def peep(self):
        return self.queue[-1],self.queue
q=queue_implementation()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()
q.peep()