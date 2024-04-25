class CircularQueue:
    def __init__(self,max):
        self.max = max
        self.items = max*[None]
        self.start = -1
        self.top = -1
        
    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)
    
    def isFull(self):
        if(self.top+1==self.start): # THIS IS FOR OCATIONS THAT THE TOP IS < START
            return True
        elif(self.start ==0 and self.top == self.max -1):
            return True
        else:
            return False
        
    def isEmpty(self):
        if(self.top == -1):
            return True
        else:return False
        
    def Enqueue(self,value):
        if (self.isFull):
            return "Sorry the list is full.cannot add values any more"
        else:
            self.top =+1
            if self.start ==-1:
                self.start = 0
            self.items[self.top] = value
            return "The value is entered"
    
    def Dequeue(self):
        if(self.isEmpty):
            return " The queue is empty"
        else:pass # for now it is passing
        