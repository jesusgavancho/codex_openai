class Graph():
  
  def __init__(self, size):
    self.adj = [ [0] * size for i in range(size)]
    self.size = size

  def add_edge(self, orig, dest):
    if orig > self.size or dest > self.size or orig < 1 or dest < 1:
      print("Invalid Edge")
    else:
      self.adj[orig-1][dest-1] = 1
      self.adj[dest-1][orig-1] = 1

  def remove_edge(self, orig, dest):
    if orig > self.size or dest > self.size or orig < 1 or dest < 1:
      print("Invalid Edge")
    else:
      self.adj[orig-1][dest-1] = 0
      self.adj[dest-1][orig-1] = 0
        
  def display(self):
    for row in self.adj:
      print("\n city or row",end='') 
      for val in row:
        print('{:2}'.format(val),end='')
      
        
        
        
a = Graph(10) 


a.add_edge(1,6)
a.add_edge(1,11)
a.display() #2,4 : 4,2