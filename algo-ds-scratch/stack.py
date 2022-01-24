'''
Write  your code


Push

MinMaxStack


st = [(1,1,1), (1,2,3)]


self.st[-1][2]

0   1   2
(9  1  10)
1
8
7

(7   7     10)
10  None None 



'''

class Stack:
  def __init__(self):
    self.st = []

  def pop(self):
    if(self.isEmpty()):
      raise Exception("stack is empty!")
    else:
      element =  self.st[-1]
      del self.st[-1]
      return element

  def push(self, key):
    if(len(self.st) < 0):
      raise Exception("stack is full!")
    else:
      min = self.getMin()
      max = self.getMax() 
      # Handling Min 
      if(min is None or key < min):
        min = key
      if(max is None or key > max):
        max = key 

      self.st.append((key, min, max))


  def getMin(self):
    if(self.st):
      return self.st[-1][1]
    else:
      return None
  
  def getMax(self):
    if(self.st):
      return self.st[-1][2]
    else:
      return None

  
  def peek(self):
    return self.st[-1]

  def isEmpty(self):
    if(self.st is None):
      return True

  def printStack(self):
    for v in self.st:
      print(v)


if __name__ == "__main__":
  st = Stack()
  st.push(3)
  st.push(4)
  
  st.push(1)
  st.push(101)
  st.push(56)

  st.printStack()


