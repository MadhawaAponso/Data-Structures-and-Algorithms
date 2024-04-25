class Queue:
    def __init__(self):
        self.items = []
        
    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)
    
    def isEmpty(self):
        if self.items == []:
            return True
        else:return False
    
    def enqueue(self,value):
        self.items.append(value)
        return "The value is added"
    
    
    def Dequeue(self):
        if(self.isEmpty()):
            return "The Queue is empty"
        else:return self.items.pop(0)
        
    def Peek(self):
        if(self.isEmpty()):
            return "The queue is empty"
        else:
            return self.items[0]
        
    def Delete(self):
        self.items = None
    
    
my_queue = Queue()

print("Before adding values:", str(my_queue.isEmpty()))
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.Dequeue()

print("After adding values:", str(my_queue.isEmpty()))

print(my_queue.Peek())


print(my_queue)
        