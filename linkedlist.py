class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next
class Linkedlist:
    def __init__(self):
        self.head = None
    def add_front(self,data):
        self.head = Node(data,self.head)
    def add_end(self,data):
        if not self.head:
            self.head=Node(data,None)
            return
        curr = self.head
        while curr.next:
            curr=curr.next
        curr.next = Node(data,None)
    def get_lastNode(self):
        n = self.head
        while(n.next != None):
            n = n.next
        return n.data
    def is_empty(self):
        return self.head == None
    def print(self):
        n = self.head
        while n!=None:
            print(n.data,end =' => ' )
            n = n.next
        print()

s = Linkedlist()
s.add_end(5)
s.add_front(8)
s.add_end(11)
print(s.is_empty())
print(s.get_lastNode())
s.print()