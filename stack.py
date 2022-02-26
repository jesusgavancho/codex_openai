class Stack:
    def __init__(self):
        self.items = []
    def empty(self):
        return self.items ==[]
    def push(self,values):
        return self.items.insert(0,values)
    def pop(self):
        return self.items.pop(0)
    def print(self):
        return print(self.items)
pila = Stack()   
pila.push(3)

pila.push(5)
pila.pop()
pila.print()
    
    
    
    
