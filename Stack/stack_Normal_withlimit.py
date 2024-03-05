class Stack:
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.stack = []
    
    def __str__(self):
        self.stack.reverse()
        values = [str(x) for x in self.stack]
        return '\n'.join(values)
    
    def isEmpty(self):
        if len(self.stack) ==0:
            return True
        else:return False
    
    def isFull(self):
        if(len(self.stack)==self.maxsize):
            return True
        else:return False
    
    def push(self,value):
        if self.isFull():
            self.stack.append(value)
            return "The value is successfully pushed"
        else: return"The stack is full. cannot add anymore"
    
    def pop(self):
        if len(self.stack) == 0 : 
            return "The stack is empty"
        else:
            value = self.stack.pop(-1)
            return value
    
    def delete(self):
        self.stack = None
        
