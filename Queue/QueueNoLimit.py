class Queue:
    def __init__(self):
        self.itmes = []
    
    def __str__(self):
        s_values = [str(x) for x in self.itmes]
        return " ".join(s_values)
    
    def IsEpmty(self):
        if not self.itmes:
            return True
        else:return False
    
    def Enqueue(self,data):
        self.itmes.append(data)
        return " The value is added"
    
    def Dequeue(self):
        if self.isEmpty():
            return " The Queue is empty"
        else:
            return self.itmes.pop(0)  #O(N) complexity
        
    def Peek(self):
        if self.isEmpty():
            return " The Queue is empty"
        else:return self.itmes[0]
        
    def Delete(self):
        if self.isEmpty():
            return " The Queue is empty"
        else:self.itmes = None

l = Queue()
l.Enqueue(1)
l.Enqueue(2)
l.Enqueue(3)
l.Enqueue(4)
print(l)