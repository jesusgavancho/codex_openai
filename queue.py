class Queue:
    def __init__(self):
        self.items= []
    def empty(self):
        return self.items ==[]
    def enqueue(self,values):
        return self.items.insert(0,values)
    def dequeue(self):
        return self.items.pop()
    def print(self):
        print(self.items)
cola = Queue()
cola.enqueue(5)
cola.enqueue(7)
cola.dequeue()
cola.print()